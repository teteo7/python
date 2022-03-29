from selenium import webdriver;
import time

#1. chromedriver 경로 설정, Chrome이 실행됨
driver= webdriver.Chrome('C:\chromedriver.exe')

#2. 원하는 페이지 입력
#driver.get("https://polartrickster.net/home")
driver.get("https://www.naver.com")

#3. 3초후에 창 닫기
#time.sleep(3)
#driver.close()

# 브라우저 종료하기 (탭 모두 종료)
#driver.quit()











