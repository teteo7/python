# 배열로 뉴스칸을 찾아서 클릭했는데 text를 찾아서 클릭하게 바꿈
# 20~ 24줄 참고

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
# li = elem.find_elements_by_tag_name("li")
# li[1].click()
li = elem.find_element_by_link_text("뉴스")
li.click()


elem = driver.find_element_by_id("snb")
Nclass = elem.find_elements_by_tag_name("a")
Nclass[1].click()

time.sleep(1)
# =================================================1

driver.execute_script('window.open("https://www.naver.com");')  #구글 창 새 탭으로 열기
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
driver.get("https://www.naver.com")

elem = driver.find_element_by_id('query')
elem.send_keys('개인정보')

elem = driver.find_element_by_class_name('btn_submit')
elem.click()

elem = driver.find_element_by_class_name("base")
li = elem.find_elements_by_tag_name("li")
li[1].click()

elem = driver.find_element_by_id("snb")
Nclass = elem.find_elements_by_tag_name("a")
Nclass[1].click()