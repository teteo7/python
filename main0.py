from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl

#1. chromedriver 경로 설정, Chrome이 실행됨
driver= webdriver.Chrome('C:\chromedriver.exe')

#2. 원하는 페이지 입력
# c= str(2)
# driver.get("https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=732")
# a = driver.find_element(By.XPATH, '//*[@id="main_content"]/div[2]/ul[1]/li['+c+']/dl/dt[2]/a')  # XPath경로값을 담음
# b = a.text  # 해당 경로에 text값 추출
# print(b)  # 텍스트값 출력

# 생성시 기본적으로 sheet1이 생성된다.
wb= openpyxl.Workbook()
sheet= wb.active

# B행4열에 입력 . . . 다음응용

# E행 3열


# By.XPath경로에 element값을 문자열로 변환해서 넣어줘야함
for a in range(1,10):
    d=str(a)
    driver.get("https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=732")
    b = driver.find_element(By.XPATH, '//*[@id="main_content"]/div[2]/ul[1]/li['+d+']/dl/dt[2]/a')  # XPath경로값을 담음
    c = b.text  # 해당 경로에 text값 추출
    sheet.cell(row=a, column=5).value = c
    print(c)  # 텍스트값 출력

driver.close()

wb.save('pyxlmain.xlsx')

#main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(1) > dl > dt:nth-child(2) > a
#main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(2) > dl > dt:nth-child(2) > a

# //*[@id="main_content"]/div[2]/ul[1]/li[1]/dl/dt[2]/a
# //*[@id="main_content"]/div[2]/ul[1]/li[2]/dl/dt[2]/a
#                                         ㄴ여기

