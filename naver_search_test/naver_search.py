from selenium import webdriver;
import time

#1. chromedriver 경로 설정, Chrome이 실행됨
driver= webdriver.Chrome('C:\chromedriver.exe')

#2. 원하는 페이지 입력
#driver.get("https://polartrickster.net/home")
driver.get("https://www.naver.com")

elem = driver.find_element_by_id('query')
elem.send_keys('DDoS')

elem = driver.find_element_by_class_name('btn_submit')
elem.click()

elem = driver.find_element_by_class_name("base")
li = elem.find_elements_by_tag_name("li")
li[1].click()

elem = driver.find_element_by_id("snb")
Nclass = elem.find_elements_by_tag_name("a")
Nclass[1].click()

driver.execute_script('window.open("naver.com");')  #구글 창 새 탭으로 열기
time.sleep(1)
#3. 3초후에 창 닫기
#time.sleep(3)
driver.close()

# 브라우저 종료하기 (탭 모두 종료)
#driver.quit()