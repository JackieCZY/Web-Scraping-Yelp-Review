#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 18:08:55 2022

@author: chenzhiyi
"""

from selenium import webdriver
import datetime
import os
import pandas as pd
import re
import time
import datetime

# libraries to crawl websites
from bs4          import BeautifulSoup
from selenium     import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def review_scrap(your_path, web_link):
    driver = webdriver.Chrome(executable_path=your_path)
    driver.get(web_link)
    reviews_one_store = []    
    while True:    
        #inspect your website
        reviews = driver.find_elements(By.XPATH, "//div[@class=' review__09f24__oHr9V border-color--default__09f24__NPAKY']")
   
        for r in range(len(reviews)):
            one_review = {}
            one_review['scrapping_date']= datetime.datetime.now()
            one_review['google_url'] = driver.current_url
        
            soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'))

            try:
                one_review_raw = reviews[r].get_attribute('innerHTML')
            except:
                one_review_raw = ""
            one_review['review_raw'] = one_review_raw
    
            try:
                one_review_text = soup.find('span', attrs={'class':'raw__09f24__T4Ezm'}).text
            except:
                one_review_text = ""
            one_review['one_review_text'] = one_review_text
    
            try:
                one_review_stars = re.findall('[0-9] [Ss]tar [rR]ating',reviews[r].get_attribute('innerHTML'))[0]
            except:
                one_review_stars = ""
            one_review['one_review_stars'] = one_review_stars
            reviews_one_store.append(one_review)
        try:
            next_button=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='icon--24-chevron-right-v2 navigation-button-icon__09f24__Bmrde css-1kq79li']")))
        except TimeoutException:
            break
        next_button.click()
        time.sleep(2)