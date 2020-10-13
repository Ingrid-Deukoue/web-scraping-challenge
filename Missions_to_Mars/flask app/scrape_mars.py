
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd


#Navigation set up
executable_path = {"executable_path": "C:/Users/ideuk/Downloads/chromedriver_win32/chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# Browse the NASA Mars News Site
mars_url = "https://mars.nasa.gov/news/"
browser.visit(mars_url)
html = browser.html
soup = BeautifulSoup(html, "html.parser")
slide_element = soup.select_one("ul.item_list li.slide")


# Assign the text to variables that you can reference later.
article = soup.find("div", class_='list_text')
news_title = slide_element.find("div", class_="content_title").get_text()
news_p = slide_element.find("div", class_="article_teaser_body").get_text()
print(news_title)
print(news_p)


# Visit Space images website
image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(image_url)
html = browser.html
soup = BeautifulSoup(html, "html.parser")



#Use splinter to navigate the site and find the image url for the current Featured Mars Image 
#assign the url string to a variable called

image = soup.find("img", class_="thumb")["src"]
featured_image_url = "https://www.jpl.nasa.gov" + image
print(featured_image_url)


#Visit the Mars Facts webpage
#se Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
facts_url = "https://space-facts.com/mars/"
browser.visit(facts_url)
mars_info = pd.read_html(facts_url)
mars_info = pd.DataFrame(mars_info[0])
mars_info.columns = ["Mars Facts", "Value"]
mars_info


# Use Pandas to convert the data to a HTML table string
mars_facts = mars_info.to_html(header = False, index = False)
print(mars_facts)

# Visit the USGS Astrogeology site
# obtain high resolution images for each of Mar's hemispheres.

import time 

hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

browser.visit(hemispheres_url)
html = browser.html
soup = BeautifulSoup(html, "html.parser")
mars_hemisphere = []

products = soup.find("div", class_ = "result-list" )
hemispheres = products.find_all("div", class_="item")

for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    end_link = hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + end_link    
    browser.visit(image_link)
    html = browser.html
    soup=BeautifulSoup(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    mars_hemisphere.append({"title": title, "img_url": image_url})


mars_hemisphere





