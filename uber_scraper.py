from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

#import datetime so that we can scroll until we see 'yesterday'
from datetime import date, timedelta
import calendar

options = webdriver.ChromeOptions()
# options.add_argument("--incognito")

browser = webdriver.Chrome(r"C:\Users\Sam Christensen\Desktop\Selenium\chromedriver.exe", chrome_options=options)
browser.get('https://health.uber.com/v2/organization/f3724445-c04c-5f5a-9c9b-495c3c6555da/past')

#logging in using id's and xpath *still need to find a way to avoid recaptcha
def uber_login():
	email_login = browser.find_element_by_id('useridInput').send_keys('123easyrides@123homecares.com')
	next_button_email = browser.find_element_by_xpath("//button[@class='btn btn--arrow btn--full']")
	next_button_email.click()
	time.sleep(2)
	password_login = browser.find_element_by_id('password').send_keys('123Austin#')
	next_button_password = browser.find_element_by_xpath("//button[@class='btn btn--arrow btn--full push--top']")
	next_button_password.click()

uber_login()




#setting the weekday for today (ie. Tuesday) so that we can automate to scroll until yesterday (ie. Monday) 
today = date.today()
yesterday = today - timedelta(days = 1)
calendar.day_name[today.weekday()]  #'Wednesday'
element = browser.find_element_by_xpath("//div[contains(text()]" = yesterday)
element.location_once_scrolled_into_view

# element = driver.find_element_by_xpath("//div[@class='h9 ha hb ah bs c4 hc b0 bm b2 bo']")

print(calendar.day_name[today.weekday()])
print(calendar.day_name[yesterday.weekday()])



# driver.find_elements_by_xpath("//*[contains(text(), 'My Button')]")


# refund_element = browser.find_elements_by_xpath("//td[@class='C($primaryColor) W(51%)']")
# refunds = [x.text for x in refund_element]

# print('print:')
# print(titles
