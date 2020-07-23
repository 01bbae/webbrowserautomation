import webbrowser
import sys
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException


# print('enter website name')
# input = input()
# webbrowser.open(input)

# driver = webdriver.Chrome('./chromedriver')


# url = 'www.nike.com'
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
# webbrowser.get(chrome_path).open_new(url)


# print(time.localtime().tm_mday)


driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.nike.com/launch?s=in-stock")
print(driver.title)


elements = driver.find_elements_by_css_selector('a')
try:
    for e in elements:
        print(e.get_attribute('href'))
        if re.search('irving', e.get_attribute('href')):
            print('DONE')
            e.click()
except StaleElementReferenceException as e:
    print(e)
    
        


# driver.find_element_by_partial_link_text('irving').get_attribute("href").click()
# search_bar = driver.find_element_by_name("search")
# search_bar.clear()
# search_bar.send_keys("airforce 1")
# search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
# driver.close()