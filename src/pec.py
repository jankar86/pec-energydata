###################################################
# Written Feb 2022 by Dylan Davis
# Purpose is to grab energy usage data from
# People's Electric Coop.
#
# As configured, should grab last 3 days of data.
#
# Assuming installed on raspberry pi, debian, or ubuntu
# Should work with python on any os, but you are on your own at that point.
#
# Prerequisits
# (sudo?) pip install selenium (or pip3)
# sudo apt-get install chromium-chromedriver
# install chromium (not sure the command)
# python(3?) agscraper.py
# fill out username and password
#
# Output - zip file -> XML in same directory as script

pecUser = ""
pecPWD  = ""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json
from array import *
import warnings


#startTime = time.localtime(time.time())
chrome_options = Options()
chrome_options.add_argument("--window-size=1280x1024")
chrome_options.add_argument("--headless")
#chrome_options.add_argument("--start-maximized")

chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
warnings.filterwarnings("ignore")

baseSleep = 3

try:
    driver = webdriver.Chrome(options=chrome_options)
    null =driver.get("https://peoplesrec.smarthub.coop/Login.html")
    #assert "Northern Country Coop" in driver.title
    time.sleep(3) #give the page some time to load

#username
    print("usr")
    #elem = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/table/tbody/tr/td/form[1]/fieldset/div[1]/div/input')
    elem = driver.find_element("xpath", '/html/body/div[5]/div[3]/div/div/table/tbody/tr/td/form[1]/fieldset/div[1]/div/input')
    #elem = driver.find_element_by_id("UserName")
    elem.clear()
    elem.send_keys(pecUser)
    #time.sleep(5)

#pw
    print("pw")
    elem = driver.find_element("xpath", '/html/body/div[5]/div[3]/div/div/table/tbody/tr/td/form[1]/fieldset/div[2]/div/input')
    #elem = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/table/tbody/tr/td/form[1]/fieldset/div[2]/div/input')
    elem.clear()
    elem.send_keys(pecPWD)

#login
    print("login")
    elem = driver.find_element("xpath", '/html/body/div[5]/div[3]/div/div/table/tbody/tr/td/form[1]/fieldset/div[6]/div/button')
    #elem = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div/table/tbody/tr/td/form[1]/fieldset/div[6]/div/button')
    elem.click()
    time.sleep(baseSleep+4)

#usage
    print("usage")
    elem = driver.find_element("xpath", '/html/body/div[5]/div[2]/div/div[1]/div/div[4]/div/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[2]/td/div/ul/li[3]/span')
    #elem = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[4]/div/div[1]/div[2]/div/div[1]/div[1]/table/tbody/tr[2]/td/div/ul/li[3]/span')
    elem.click()
    time.sleep(baseSleep)

#usage explorer
    print("usage exp")
    elem = driver.find_element("xpath", '/html/body/div[5]/div[2]/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/div/button')
    #elem = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/div/button')
    elem.click()
    time.sleep(baseSleep+7)

#date range preset
    print("date range radio")
    elem = driver.find_element("xpath", '/html/body/div[5]/div[2]/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/label/input')
    #elem = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/label/input')
    elem.click()
    time.sleep(baseSleep)


#unbilled
    print("unbilled")
    elem = driver.find_element("xpath", '/html/body/div[5]/div[2]/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/div/div/div/label[1]')
   #elem = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/div/div/div/label[1]')
    elem.click()
    time.sleep(baseSleep+7)

#hourly
    print("hourly")
    elem = driver.find_element("xpath", '/html/body/div[5]/div[2]/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div[3]/div/div/div/div/div/label[3]')
    #elem = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div[3]/div/div/div/div/div/label[3]')
    elem.click()
    time.sleep(baseSleep+7)

#72 hrs
    print("72hrs")
    elem = driver.find_element("xpath", '/html/body/div[5]/div[2]/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/div/div/div/label[5]')
    #elem = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[3]/div/div[1]/div[2]/div/div/div/div/label[5]')
    elem.click()
    print("post72click")
    time.sleep(baseSleep+7)

#download - green button
    print("green btn")
    elem = driver.find_element("xpath", '/html/body/div[5]/div[2]/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div[2]/div/img')
    #elem = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div[2]/div/img')
    elem.click()
    time.sleep(baseSleep+3)

#download
    print("download")
    elem = driver.find_element("xpath", '/html/body/div[7]/div/div/div[3]/button[2]')
    #elem = driver.find_element_by_xpath('/html/body/div[7]/div/div/div[3]/button[2]')
    elem.click()
    time.sleep(15)  #give file plenty of time to download


except:
    raise
finally:
    null = driver.close() #this will close crhromium

