import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

#function to get the url
def get_url(position, location):
    template = "https://in.indeed.com/jobs?q={}&l={}&vjk"
    result = template.format(position, location)
    return result

#function to scrap data
def get_record(card):
    job_title = card.find("a", {"class": "jcs-JobTitle"}).string
    company_name = card.find("span", {"class": "companyName"}).get_text()
    job_location = card.find("div", {"class": "companyLocation"}).text
    description = card.find("div", {"class": "job-snippet"}).text
    post_date = card.find("span", {"class": "date"}).text
    today = datetime.today().strftime("%y-%m-%d")

    #all sections doesn't have salary so used try catch block to avoid errors
    try:
        salary = card.find("div", {"metadata salary-snippet-container"}).text
    except AttributeError:
        salary = ""

    #to find the link of each jobs
    job_href = card.find("a", {"class": "jcs-JobTitle"}).get("href")
    job_url = "https://in.indeed.com" + job_href

    result= (job_title, company_name, job_location, description, post_date, today, salary, job_url)

    return result


def main(position,location):

    records=[]

    url=get_url(position,location)

    #this will help to iterate over each pages until ">" button is not found
    while True:
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.find_all("div", {"class": "slider_container css-11g4k3a eu4oa1w0"})

        for card in cards:
            record = get_record(card)
            records.append(record)

        # getting next page
        try:
            url = "https://in.indeed.com" + soup.find("a", {"aria-label": "Next"}).get("href")
        except AttributeError:
            break

    return records

#taking user input
pos=input("Enter Job Position: ")
loc=input("Enter Job Location: ")

#storing like this to convert into .xlsx file
job_titles=[]
company_names=[]
job_locations=[]
descriptions=[]
post_dates=[]
todays=[]
salarys=[]
job_urls=[]

for element in main(pos,loc):
    job_titles.append(element[0])
    company_names.append(element[1])
    job_locations.append(element[2])
    descriptions.append(element[3])
    post_dates.append(element[4])
    todays.append(element[5])
    salarys.append(element[6])
    job_urls.append(element[7])

indeed_df=pd.DataFrame({"Job Title":job_titles, "Company Name":company_names, "Job Locations":job_locations, "Job Description":descriptions, "Posted":post_dates, "Today's Date":todays, "Salary":salarys, "Job Link":job_urls})

indeed_df.to_excel("imdb_data.xlsx", index=False)