# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, time
from bs4 import BeautifulSoup

start_time = datetime.now()

browser = webdriver.Chrome(executable_path="chromedriver")

browser.get('https://www.sahibinden.com')
#By.XPATH, "/html/body/div[3]/div/p/a/"

link = browser.find_elements(By.XPATH, "/html/body/div[3]/div/p/a")[0]

get_link = link.get_attribute("href")

browser.execute_script("get_link.setAttribute('href', 'yunusadas');")

newlink = link.get_attribute("href")

print(newlink)

#'https://yunusadas.com'





