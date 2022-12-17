
# INDEED JOBS SCRAPPER
## A Multi-Page Scraper made with the help of Beautiful Soup 🧾

![](https://media4.giphy.com/media/HOyxA78TV7ZTnLDetj/giphy.gif?cid=ecf05e475kjgcmgii8s4ry06fhdvdjk3a1wbl87wsodf1u8e&rid=giphy.gif&ct=s)

## Table of Contents

1.  [Overview](#Overview)
 
2.  [Libraries Used](#Libraries-Used)
3.  [Workflow](#Workflow)
4.  [Screenshots](#Screenshots)
5.  [Challenges](#Challenges)

## Overview

"Indeed" is one of the most popular job websites in the market today. Scraping "Indeed" job data can help us access the latest job data, analyze job trends, and automate job boards. "Indeed" allows us to search job-based on location and keywords. I will be using job title and job location along with the number of pages of search results to crawl "Indeed" and extract the data.


## Libraries-Used

-   `requests`
-   `BeautifulSoup`
-   `datetime`
-   `pandas`

## Workflow

- **Accessing** https://in.indeed.com/ via the 'requests' library.
- Getting the **"Job Title" and "Job Location"** as per the users choice.
- **Formatting** the url to a dynamic url where "Job Title" and "Job Location" can be changed.
- **Scraping** the *Job Title, Company Name, Job Locations, Job Description, Posted Date, Salary, Job Link* for each of the jobs.
- **Navigating** to the next page using pagination techniques.
- **Converting** the scrapped data to .xlsx file using the `pandas` library.

## Screenshots

- Giving the user input.

![](https://media.giphy.com/media/RgWMAkAZzddhs5O2xM/giphy.gif)

- The output file.

![](https://media.giphy.com/media/CkAF8XZ4LRxqp3la1f/giphy.gif)


## Challenges
There were some AttributeErrors so had to use try catch block to overcome it.

### Thankyou For Spending Your Precious Time Going Through This Project!
### If You Find Any Value In This Project Or Gained Something New Please Do Give A ⭐.
