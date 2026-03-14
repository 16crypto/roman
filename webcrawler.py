import requests              # used to send HTTP requests
from bs4 import BeautifulSoup   # used to parse HTML pages

# function to crawl a webpage
def crawl(url):

    # Step 1: send request to website
    response = requests.get(url)

    # Step 2: parse the HTML content of webpage
    soup = BeautifulSoup(response.text, "html.parser")

    print("Links found on:", url)

    # Step 3: find all anchor tags <a>
    for link in soup.find_all("a"):

        # extract href attribute from link
        href = link.get("href")

        # check if link exists
        if href:
            print(href)

# starting webpage
url = "https://example.com"

# call crawler
crawl(url)