from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_news = {}

    #scrape news info
    url = 'https://mars.nasa.gov/news/'
    #open chrome using chorme driver
    browser.visit(url)
    time.sleep(1)

    #scrape browser
    html = browser.html
    soup = bs(html,'html.parser')
    news_title = soup.find("ul", class_="item_list").find("div", class_="content_title").text
    news_p = soup.find("ul", class_="item_list").find("div", class_="article_teaser_body").text
    mars_news["title"] = news_title
    mars_news["paragraph"] = news_p

    #scrape featured image
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    base_url = "https://www.jpl.nasa.gov"
    browser.visit(url2)
    time.sleep(1)
    html2 = browser.html
    soup = bs(html2,'html.parser')
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(1)
    html3 = browser.html
    soup = bs(html3,'html.parser')
    imgpath = soup.find("img", class_="fancybox-image")["src"]
    mars_news["img"] = base_url+imgpath

    #scrape mars facts
    url3 = "https://space-facts.com/mars/"
    tables = pd.read_html(url3)[0]
    tables.columns = ['measure', 'value']
    mars_news["table"] = tables.to_html(index = False).replace("text-align: right;", "text-align: center;").replace("\n", "")

    #scrpae mars hemisphere
    url4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url4)
    time.sleep(1)
    html4 = browser.html
    soup = bs(html4,'html.parser')
    base_url4 = "https://astrogeology.usgs.gov"
    href = []
    test = soup.find_all("div", class_="description")
    for row in test:
        href.append(base_url4 + (row.find("a", class_="itemLink product-item")["href"]))
    hemisphere_image_urls = []
    for url in href:
        browser.visit(url)
        time.sleep(1)
        html5 = browser.html
        soup = bs(html5,'html.parser')
        title = soup.find("h2", class_="title").text
        img_url = base_url4 + soup.find("img", class_="wide-image")["src"]
        hemisphere_image_urls.append({"title":title, "img_url":img_url})
        time.sleep(1)
    mars_news["hemisphere"] = hemisphere_image_urls

    browser.quit()
    return mars_news