# from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from webdriver_manager.chrome import ChromeDriverManager
#
# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
#
# # from selenium.webdriver.common.by import By
# # PATH = "/usr/local/bin/chromedriver"
# # driver = webdriver.Chrome(PATH)
#
# # driver.maximize_window()
# # # login = driver.find_element_by_css_selector("a.header-login")
# #
# # driver.get("https://www.udemy.com/")
# # # driver.find_element_by_xpath("//span[normalize-space()='Login']")
#
# # driver.find_element(by=By.XPATH, value="//span[normalize-space()='Login']").click()
#
# # pip install webdriver-manager

"""from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get('https://www.google.com')
driver.find_element(By.NAME, 'q').send_keys('Yasser Khalil')
driver.__enter__()
time.sleep(30)
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.kai.id/')

# driver.find_element(By.XPATH, "(//span[@id='select2-origination2-container'])[1]").click()
# driver.find_element(By.XPATH, "(//input[@role='textbox'])[1]").send_keys("Bandung")
# driver.find_element(By.XPATH, "(//input[@role='textbox'])[1]").send_keys(Keys.RETURN)