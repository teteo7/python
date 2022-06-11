import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time



service = Service('C:\chromedriver.exe')
service.creationflags = subprocess.CREATE_NO_WINDOW

options= webdriver.ChromeOptions()
# options.add_argument('--headless') #크롬창이 뜨지 않음
# options.add_argument('window-size=1920x500') # 윈도우 창 설정
options.add_argument("disable-gpu") #크롬 가속화, cpu와 gpu를 이용해 랜더링 가속화 자원,랜더링 효율

#1. chromedriver 경로 설정, Chrome이 실행됨
driver= webdriver.Chrome('C:\chromedriver.exe', chrome_options=options, service=service)

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