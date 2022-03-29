from selenium import webdriver
from selenium.webdriver.common.by import By


#1. chromedriver 경로 설정, Chrome이 실행됨
driver= webdriver.Chrome('C:\chromedriver.exe')



#2. 원하는 페이지 입력
driver.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8")


#이게 구방식인데 더편하다.
# a= driver.find_element_by_xpath('//*[@id="main_pack"]/section[1]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/strong') #XPath경로값을 담음
# b= a.text #해당 경로에 text값 추출
# print(b) #텍스트값 출력

#이게 최신 방식인데 아직 적응 안됨. driver.find_elements()는 여러개 불러오는건가?
#driver.find_element(By.XPATH, XPATH)의 By부분 import로 함수 가져와야함
a= driver.find_element(By.XPATH, '//*[@id="main_pack"]/section[1]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/strong'); #XPath경로값을 담음
b= a.text #해당 경로에 text값 추출
print(b) #텍스트값 출력

driver.close()

