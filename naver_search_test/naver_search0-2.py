import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import chromedriver_autoinstaller
import os

wdpath = chromedriver_autoinstaller.install(cwd=True) # 자동으로 chromedriver 설치
wdpath = wdpath.replace("\\", "\\\\")



# service = Service('C:\chromedriver.exe')
service= Service()
service.creationflags = subprocess.CREATE_NO_WINDOW # 새 프로세스가 창을 만들지 않도록 지정하는 Popen creationflags 매개 변수.

options= webdriver.ChromeOptions()
# options.add_argument('--headless') #크롬창이 뜨지 않음
# options.add_argument('window-size=1920x500') # 윈도우 창 설정
options.add_argument("disable-gpu") #크롬 가속화, cpu와 gpu를 이용해 랜더링 가속화 자원,랜더링 효율
options.add_experimental_option("detach", True)

#1. chromedriver 경로 설정, Chrome이 실행됨
driver= webdriver.Chrome(wdpath, chrome_options=options, service=service)

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
li = elem.find_element_by_link_text("뉴스")
li.click()

elem = driver.find_element_by_id("snb")
Nclass = elem.find_elements_by_tag_name("a")
Nclass[1].click()

pid = driver.service.process.pid
os.system("taskkill /f /im chromedriver.exe /t")

# os.system("taskkill /pid {} /t".format(11316))
# taskkill /f /im chromedriver.exe /t