#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:44:07 2018

@author: vicky
"""

from selenium import webdriver     
 
# For using sleep function because selenium 
# works only when the all the elemets of the 
# page is loaded.
import time 
  
from selenium.webdriver.common.keys import Keys 
 
# Creating an instance webdriver
browser = webdriver.Chrome() 
browser.get('https://www.twitter.com')
 
# Let's the user see and also load the element 
#time.sleep(2)

login = browser.find_elements_by_xpath('//*[@id="doc"]/div/div[1]/div[1]/div[2]/div/a')
 
# using the click function which is similar to a click in mouse.
login[0].click()
 
print("Loggin in Twitter")
 
user = browser.find_elements_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
 
# Enter User Name
user[0].send_keys('YOUR USERNAME')
 
user = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')

# Reads password from a text file because
# saving the password in a script is just silly.
with open('test.txt', 'r') as myfile:  
    Password = myfile.read().replace('\n', '')
user.send_keys(Password)
 
LOG = browser.find_elements_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
LOG[0].click()
print("Login Sucessfull")

time.sleep(5)
elem = browser.find_element_by_xpath('//*[@id="tweet-box-home-timeline"]')

#elem = browser.find_element_by_xpath('//*[@id="search-query"]')
elem.click()
elem.clear()

elem = browser.find_element_by_xpath('//*[@id="tweet-box-home-timeline"]')
 
elem.send_keys('This is my first twitter automation script and this post has been posted by my automated software !')

tweet = browser.find_elements_by_xpath('//*[@id="timeline"]/div[2]/div/form/div[3]/div[2]/button/span[1]')
tweet[0].click()

print ("Tweet Posted Successfully")
# using keys to send special KEYS 
#elem.send_keys(Keys.RETURN) 
 
print("Task Done Sucessfully")
 
# closing the browser
time.sleep(10)
# closing the browser
browser.close() 
