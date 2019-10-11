from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd


def scrape():

    executable_path = {'executable_path': 'C:/Users/Bin/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    url = 'https://mars.nasa.gov/news/'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    results = soup.find_all('div', class_="slide")

    for result in results:
        title = result.find('div', class_="content_title")
        news_title = title.find('a').text.strip()
        paragraph = result.find('div', class_="rollover_description_inner").text.strip()


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    results = soup.find_all('a', class_='button fancybox')

    image = []
    main_url = 'https://www.jpl.nasa.gov'

    for x in results:
        picture = x['data-fancybox-href']
        image.append(picture)
    
        featured_image_url = main_url + picture


    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    weather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text.strip()



    





    mars_HW = {'title': news_title, 'paragraph': paragraph, 'featured_image_url': featured_image_url, 'weather': weather}
    return mars_HW


