# WEB SCRAPPER


import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.shadowfox.in/")
print(url.content)

web = BeautifulSoup(url.content,"html.parser")

print(web.prettify())               #   formatted data with prettify

#  Website Title
print(web.title)

#  Website Title Name
print(web.title.name)

#  Website Title String
print(web.title.string)


################################################################
print("-------------------------- try 2--------------------------------------")

# URL of the page we want to scrape
url = "http://books.toscrape.com/"

# Sending a GET request to the website
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the content of the response
    soup = BeautifulSoup(response.content, 'html.parser')

    # Finding all book containers
    books = soup.find_all('article', class_='product_pod')

    # Extracting data from each book
    for book in books:
        title = book.h3.a['title']  # Book title
        price = book.find('p', class_='price_color').text  # Book price

        print(f'Title: {title}, Price: {price}')
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
