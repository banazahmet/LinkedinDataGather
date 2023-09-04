# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 22:15:33 2023

@author: Ahmet
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exceptions

import os, random, sys, time
from bs4 import BeautifulSoup

from IPython import get_ipython
get_ipython().magic('reset -sf')

import webbrowser
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://www.linkedin.com/uas/login')

file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]

time.sleep(5)

elementID = browser.find_element_by_id('username')
elementID.send_keys(username)
elementID = browser.find_element_by_id('password')
elementID.send_keys(password)
elementID.submit()

needPath = 'matlab headhunter'
search_term = needPath;
search_term = search_term.split()
linkedin_search = search_term[0] + '%20' + search_term[1]# + '%20' + search_term[2]
linkedin_search_baseurl = "https://www.linkedin.com/search/results/people/?keywords="
time.sleep(3)

linkedin_pages = '&page='+str(1)
browser.get(linkedin_search_baseurl + linkedin_search + linkedin_pages)
time.sleep(3)