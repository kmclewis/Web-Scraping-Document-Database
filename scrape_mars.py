#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import time



def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data = {}
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)


    html = browser.html
        # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    articles = soup.find('div', class_='content_title')


    link = articles.find('a')
    href = link['href']
    news_title = link.string

    teaser = soup.find('div', class_='article_teaser_body')
    news_p = teaser.string

    
    print(news_title)
    print(news_p)
    mars_data["title"] = news_title
    mars_data["teaser"] = news_p

    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)

    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')


    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5) 
    browser.click_link_by_partial_text('more info')


    new_url = browser.url
    browser.visit(new_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    image =soup.find_all('figure', class_='lede')
   
    link = image[0].find('a')
    href = link['href']
    image_url = 'https://jpl.nasa.gov'+ href
    
    mars_data["image"] = image_url

    mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_weather_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    tweet = soup.find_all('div', class_='stream-container')


    paragraph=tweet[0].find('p')
    mars_weather = paragraph.text
    print(mars_weather)

    mars_data["weather"] = mars_weather


    mars_facts_url = 'https://space-facts.com/mars/'
    browser.visit(mars_facts_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    tables = pd.read_html(mars_facts_url)

    df = tables[0]
    df.columns = ['description', 'value']
    df.set_index('description', inplace=True)


    html_table = df.to_html()
    html_table

    mars_data_table = html_table.replace("\n", "")
    mars_data["table"] = mars_data_table    
    
    mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemispheres_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(5)
    browser.click_link_by_partial_text('Cerberus Hemisphere')

    new_url = browser.url
    browser.visit(new_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    cerberus = soup.find_all('div', class_='downloads')
    cerberus_link = cerberus[0].find('a')
    cerberus_href = cerberus_link['href']
    cerberus_href

    mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemispheres_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(5)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere')

    new_url = browser.url
    browser.visit(new_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    schiaparelli = soup.find_all('div', class_='downloads')
    schiaparelli_link = schiaparelli[0].find('a')
    schiaparelli_href = schiaparelli_link['href']
    schiaparelli_href

    mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemispheres_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(5)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere')

    new_url = browser.url
    browser.visit(new_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    syrtis_major = soup.find_all('div', class_='downloads')
    syrtis_major_link = syrtis_major[0].find('a')
    syrtis_major_href = syrtis_major_link['href']
    syrtis_major_href

    mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemispheres_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(5)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere')

    new_url = browser.url
    browser.visit(new_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    valles_marineris = soup.find_all('div', class_='downloads')
    valles_marineris_link = valles_marineris[0].find('a')
    valles_marineris_href = valles_marineris_link['href']
    valles_marineris_href

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": valles_marineris_href},
        {"title": "Cerberus Hemisphere", "img_url": cerberus_href},
        {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_href},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_major_href},]

    mars_data["spheres"] = hemisphere_image_urls    

    browser.quit()
    return mars_data

