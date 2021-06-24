#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import packages 
import time
import re
import string 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter


# In[2]:


#Load workbook data
wb = load_workbook(filename = 'input.xlsx')
sheet = wb.active


# In[3]:


#Prepare destinations
destinations = []
for cell in ['C1','D1','E1']:
    destinations.append(sheet[cell].value)


# In[4]:


def scrape_distance(driver):
    wait.until(presence_of_element_located((By.CSS_SELECTOR, "#pane > div > div.widget-pane-content.cYB2Ge-oHo7ed > div > div > div.section-layout")))
    distances = driver.find_elements_by_class_name('section-directions-trip-distance')
    distance = re.sub("[^0-9.]", "", distances[0].text) #Take first distance
    return distance


# In[5]:


#Start web scraping
print("Starting Chrome....")
with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    startTime = time.time()
    
    row = 2  #starting from row 2 in excel
    origin_zipcode = ""
    NUMBER_OF_DESTINATION_COLUMNS = 3
    
    while row < 501:
        origin_zipcode = sheet['B'+ str(row)].value
        if origin_zipcode != None:
            for i in range(NUMBER_OF_DESTINATION_COLUMNS): 
                driver.get(f"https://www.google.com/maps/dir/Japan,+〒{origin_zipcode}/{destinations[i]}")
                walking_button = driver.find_elements_by_xpath('//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[4]/button')[0]
                walking_button.click() ## Click the walking btn 
                sheet[string.ascii_uppercase[i+2]+ str(row)] = scrape_distance(driver)
        else:
            break
        sheet['F'+ str(row)] = "https://www.google.com/maps/place/〒"+ origin_zipcode
        row+=1    

    wb.save("./output.xlsx")
    print("Total time spent is ",time.time()-startTime, "secs")

