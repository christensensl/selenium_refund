from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

# this is a test to keep the send_keys stuff in the project.
# driver.find_element_by_name().send_keys(Keys.ENTER)

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

browser = webdriver.Chrome(r"C:\Users\Sam Christensen\Desktop\Selenium\chromedriver.exe", chrome_options=options)

browser.get('https://finance.yahoo.com/quote/FB?p=FB')
# timeout = 10
# try:
# 	WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='Va(m) C(black) Wow(bw) Us(n)'']")))
# except TimeoutException:
# 	print("Timed out waiting for page to load")
# 	browser.quit()

# use datareactID and create a dictionary like in mikey's code. 

titles_element = browser.find_elements_by_xpath("//td[@class='C($primaryColor) W(51%)']")
titles = [x.text for x in titles_element]

print('titles:')
print(titles)

values_elements = browser.find_elements_by_xpath("//td[@class='Ta(end) Fw(600) Lh(14px)']")
values = [x.text for x in values_elements]

print('values:')
print(values, '\n')

for title, value in zip(titles, values):
	print(title + ': ' + value)