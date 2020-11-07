# web-scraping-challenge

## Background
The purpose of this project is to build a python module that will scrap current Mars data from the the internet and display the changes on the website when a user clicks a button. All of the data will be scrapped from  [the NASA Jet Propulsion Laboratory Website](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) and [the astrogeology website](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars).

## Methods
Languages that were used for this projects are **HTML** and **Python** with libraries like **Flask, PyMongo, Splinter and BeautifulSoup**.  
1. Splinter & Chromedriver were used to navigate through the websites.
2. BeautifulSoup was used to scrap necessary data from the website.
3. Scrapped data were stored in Pymongo.
4. Using Flask, all the stored data are displayed on the formatted html website.

## Preview
![](mars.gif)
