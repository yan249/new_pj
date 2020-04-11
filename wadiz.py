import time 

from selenium import webdriver
browser = webdriver.Chrome('./chromedriver')
browser.get("https://www.wadiz.kr/web/campaign/detailBacker/62297")
time.sleep(30)

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, 'html.parser')
title_1 = soup.select('#reward-static-supports-list-app > div > div > div > div.ListContainer_container__GpvaU > div:nth-child(1) > div > p > button')
cost_1 = soup.select('#reward-static-supports-list-app > div > div > div > div.ListContainer_container__GpvaU > div:nth-child(1) > div > p > strong')

for wadiz_list_1 in zip(title_1, cost_1):
    print(wadiz_list_1[1].text, wadiz_list_1[0].text)

title_2 = soup.select('#container > div.reward-body-wrap > div > div > div.wd-ui-sub-opener-info > div.moveRewards > div > button:nth-child(3) > div > dl > dd > p.reward-name')
cost_2 = soup.select('#container > div.reward-body-wrap > div > div > div.wd-ui-sub-opener-info > div.moveRewards > div > button:nth-child(3) > div > p.reward-soldcount')

for wadiz_list_2 in zip(title_2, cost_2):
    print(wadiz_list_2[1].text, wadiz_list_2[0].text)


