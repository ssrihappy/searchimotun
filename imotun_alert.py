from selenium import webdriver

# Chrome 브라우저를 자동으로 설치하여 WebDriver를 설정
import chromedriver_autoinstaller

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

#import pandas as pd
from selenium.webdriver.common.keys import Keys
import requests

from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime


def SendMessage(msg):
    try:
            # Discord Webhook URL
        WEBHOOK_URL = 'URL'  # Discord에서 복사한 Webhook URL을 입력하세요

        # 보낼 메시지 데이터
        message_data = {
            "content": f"{msg}"
        }

        # 메시지 전송
        response = requests.post(WEBHOOK_URL, json=message_data)

    except Exception as ex:
        print(ex)


def check_imotun(): # hmp

    options = Options()
    chromedriver_autoinstaller.install()
    options.add_argument('headless')  
    driver = webdriver.Chrome(options=options)     
    id = 'HMP ID'
    pw = 'HMP PW'

    url_hmp = 'http://hmpmall.co.kr'

    #로그인
    driver.get(url_hmp)
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, '//*[@id="memId"]').send_keys(id)
    driver.find_element(By.XPATH, '//*[@id="memPw"]').send_keys(pw)
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div/div/div[2]/div[2]/ul/li[3]/a').click()
    sleep(5)
    driver.implicitly_wait(3)

    main = driver.window_handles
    for i in main:
        if i != main[0]:
            driver.switch_to.window(i)
            driver.close()
            
    driver.switch_to.window(main[0])

    sleep(1)

      #초기검색모듈 #더미검색

    actions = ActionChains(driver)
    actions.send_keys('이모튼')  # or 다른 품절약
    actions.send_keys(Keys.ENTER)         

    actions.perform() 

    sleep(1)
    driver.implicitly_wait(3)

        
    imotun_price = driver.find_element(By.XPATH, '//*[@id="mainList0"]/td[5]').text
    imotun_jaego = driver.find_element(By.XPATH, '//*[@id="selectedStock"]').text
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if str(imotun_price) != '0원' or str(imotun_jaego) != '0':

        SendMessage(f'{time} | HMP 이모튼 재고 있음')
        print('HMP 이모튼 재고 있음')
    else:

        #SendMessage(f'{time} | HMP 이모튼 재고 없음')
        #print('HMP 이모튼 재고 없음')
        pass


check_imotun()
