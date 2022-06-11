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
options.add_experimental_option("detach", True) # 자동으로 창을 닫지 않음, chromedriver_autoinstaller.install가 자동으로 브라우저를 닫는걸 취소해줌

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

time.sleep(1)
# =================================================2

driver.execute_script('window.open("https://www.naver.com");')  #구글 창 새 탭으로 열기
driver.switch_to.window(driver.window_handles[2])
time.sleep(1)
driver.get("https://www.naver.com")

elem = driver.find_element_by_id('query')
elem.send_keys('랜섬웨어')

elem = driver.find_element_by_class_name('btn_submit')
elem.click()

elem = driver.find_element_by_class_name("base")
li = elem.find_element_by_link_text("뉴스")
li.click()

elem = driver.find_element_by_id("snb")
Nclass = elem.find_elements_by_tag_name("a")
Nclass[1].click()

time.sleep(1)
# =================================================3

driver.execute_script('window.open("https://www.naver.com");')  #구글 창 새 탭으로 열기
driver.switch_to.window(driver.window_handles[3])
time.sleep(1)
driver.get("https://www.naver.com")

elem = driver.find_element_by_id('query')
elem.send_keys('바이러스')

elem = driver.find_element_by_class_name('btn_submit')
elem.click()

elem = driver.find_element_by_class_name("base")
li = elem.find_element_by_link_text("뉴스")
li.click()

elem = driver.find_element_by_id("snb")
Nclass = elem.find_elements_by_tag_name("a")
Nclass[1].click()

time.sleep(1)
# =================================================4

driver.execute_script('window.open("https://www.naver.com");')  #구글 창 새 탭으로 열기
driver.switch_to.window(driver.window_handles[4])
time.sleep(1)
driver.get("https://www.naver.com")

elem = driver.find_element_by_id('query')
elem.send_keys('보안')

elem = driver.find_element_by_class_name('btn_submit')
elem.click()

elem = driver.find_element_by_class_name("base")
li = elem.find_element_by_link_text("뉴스")
li.click()

elem = driver.find_element_by_id("snb")
Nclass = elem.find_elements_by_tag_name("a")
Nclass[1].click()

time.sleep(1)
# =================================================5

driver.execute_script('window.open("https://www.naver.com");')  #구글 창 새 탭으로 열기
driver.switch_to.window(driver.window_handles[5])
time.sleep(1)
driver.get("https://www.naver.com")

elem = driver.find_element_by_id('query')
elem.send_keys('악성코드')

elem = driver.find_element_by_class_name('btn_submit')
elem.click()

elem = driver.find_element_by_class_name("base")
li = elem.find_element_by_link_text("뉴스")
li.click()

elem = driver.find_element_by_id("snb")
Nclass = elem.find_elements_by_tag_name("a")
Nclass[1].click()

time.sleep(1)
# =================================================6

driver.execute_script('window.open("https://www.naver.com");')  #구글 창 새 탭으로 열기
driver.switch_to.window(driver.window_handles[6])
time.sleep(1)
driver.get("https://www.naver.com")

elem = driver.find_element_by_id('query')
elem.send_keys('정보보호')

elem = driver.find_element_by_class_name('btn_submit')
elem.click()

elem = driver.find_element_by_class_name("base")
li = elem.find_element_by_link_text("뉴스")
li.click()

elem = driver.find_element_by_id("snb")
Nclass = elem.find_elements_by_tag_name("a")
Nclass[1].click()

time.sleep(1)
# =================================================7

driver.execute_script('window.open("https://www.naver.com");')  #구글 창 새 탭으로 열기
driver.switch_to.window(driver.window_handles[7])
time.sleep(1)
driver.get("https://www.naver.com")

elem = driver.find_element_by_id('query')
elem.send_keys('취약점')

elem = driver.find_element_by_class_name('btn_submit')
elem.click()

elem = driver.find_element_by_class_name("base")
li = elem.find_element_by_link_text("뉴스")
li.click()

elem = driver.find_element_by_id("snb")
Nclass = elem.find_elements_by_tag_name("a")
Nclass[1].click()

time.sleep(1)
# =================================================8

driver.execute_script('window.open("https://www.naver.com");')  #구글 창 새 탭으로 열기
driver.switch_to.window(driver.window_handles[8])
time.sleep(1)
driver.get("https://www.naver.com")

elem = driver.find_element_by_id('query')
elem.send_keys('해킹')

elem = driver.find_element_by_class_name('btn_submit')
elem.click()

elem = driver.find_element_by_class_name("base")
li = elem.find_element_by_link_text("뉴스")
li.click()

elem = driver.find_element_by_id("snb")
Nclass = elem.find_elements_by_tag_name("a")
Nclass[1].click()

time.sleep(1)
# =================================================9

driver.execute_script('window.open("https://www.naver.com");')  #구글 창 새 탭으로 열기
driver.switch_to.window(driver.window_handles[9])
time.sleep(1)
driver.get("https://www.naver.com")

elem = driver.find_element_by_id('query')
elem.send_keys('유출')

elem = driver.find_element_by_class_name('btn_submit')
elem.click()

elem = driver.find_element_by_class_name("base")
li = elem.find_element_by_link_text("뉴스")
li.click()

elem = driver.find_element_by_id("snb")
Nclass = elem.find_elements_by_tag_name("a")
Nclass[1].click()

time.sleep(1)

# =================================================10

driver.execute_script('window.open("https://www.naver.com");')  #구글 창 새 탭으로 열기
driver.switch_to.window(driver.window_handles[10])
time.sleep(1)
driver.get("https://www.naver.com")

elem = driver.find_element_by_id('query')
elem.send_keys('복원')

elem = driver.find_element_by_class_name('btn_submit')
elem.click()

elem = driver.find_element_by_class_name("base")
li = elem.find_element_by_link_text("뉴스")
li.click()

elem = driver.find_element_by_id("snb")
Nclass = elem.find_elements_by_tag_name("a")
Nclass[1].click()

time.sleep(1)
# =================================================11

driver.execute_script('window.open("https://www.naver.com");')  #구글 창 새 탭으로 열기
driver.switch_to.window(driver.window_handles[11])
time.sleep(1)
driver.get("https://www.naver.com")

elem = driver.find_element_by_id('query')
elem.send_keys('통신사')

elem = driver.find_element_by_class_name('btn_submit')
elem.click()

elem = driver.find_element_by_class_name("base")
li = elem.find_element_by_link_text("뉴스")
li.click()

elem = driver.find_element_by_id("snb")
Nclass = elem.find_elements_by_tag_name("a")
Nclass[1].click()

# =================================================12

driver.execute_script('window.open("https://www.naver.com");')  #구글 창 새 탭으로 열기
driver.switch_to.window(driver.window_handles[12])
time.sleep(1)
driver.get("https://www.naver.com")

elem = driver.find_element_by_id('query')
elem.send_keys('다크웹')

elem = driver.find_element_by_class_name('btn_submit')
elem.click()

elem = driver.find_element_by_class_name("base")
li = elem.find_element_by_link_text("뉴스")
li.click()

elem = driver.find_element_by_id("snb")
Nclass = elem.find_elements_by_tag_name("a")
Nclass[1].click()

# =================================================13

driver.execute_script('window.open("https://www.naver.com");')  #구글 창 새 탭으로 열기
driver.switch_to.window(driver.window_handles[13])
time.sleep(1)
driver.get("https://www.naver.com")

elem = driver.find_element_by_id('query')
elem.send_keys('크리덴셜')

elem = driver.find_element_by_class_name('btn_submit')
elem.click()

elem = driver.find_element_by_class_name("base")
li = elem.find_element_by_link_text("뉴스")
li.click()

elem = driver.find_element_by_id("snb")
Nclass = elem.find_elements_by_tag_name("a")
Nclass[1].click()

# os.system('pause')

#3. 3초후에 창 닫기
#time.sleep(3)
#driver.close()

# 브라우저 종료하기 (탭 모두 종료)
#driver.quit()