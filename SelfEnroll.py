from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

cmdUsername = input('What is your username?')
cmdPassword = input('What is your password?')
cmdCRN = input('What is the CRN of the course you would like to sign up for?')
cmdTime = input('How often (in seconds) would you like to check availability?')
cmdTime = int(cmdTime)

count = 0

while (count < 1):
    browser = webdriver.Firefox()
    time.sleep(2)
    browser.get('www.google.com')
    time.sleep(2)
    browser.get('wwwp.oakland.edu')
    time.sleep(2)
    browser.get('http://wwwp.oakland.edu/r/mysail')
    time.sleep(2)
    usr = browser.find_element_by_id('username')
    usr.send_keys(cmdUsername)
    time.sleep(2)
    pswd = browser.find_element_by_id('password')
    pswd.send_keys(cmdPassword)
    time.sleep(2)
    pswd.send_keys(Keys.ENTER)
    time.sleep(2)
    browser.get('https://sail.oakland.edu/PROD/twbkwbis.P_GenMenu?name=bmenu.P_RegMnu')
    time.sleep(2)
    btnAdd = browser.find_element_by_id('contentItem11')
    btnAdd.click()
    time.sleep(2)
    option = browser.find_element_by_xpath("//select[@id='term_id']/option[@value='201610']")
    option.click()
    time.sleep(2)
    btnTermSub = browser.find_element_by_id('id____UID7')
    btnTermSub.click()
    time.sleep(2)
    txtCRN = browser.find_element_by_id('crn_id1')
    txtCRN.send_keys(cmdCRN)
    # Put the check in here
    time.sleep(2)
    btnCRN = browser.find_element_by_id('id____UID5')
    btnCRN.click()
    time.sleep(2)
    browser.close()
    time.sleep(cmdTime)
