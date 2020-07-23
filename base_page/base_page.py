from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# def open_browser(browser_type):
#     browser_type = browser_type.upper()
#     if browser_type =="CHR":
#         driver = webdriver.Chrome()
#     elif browser_type == "IE":
#         driver = webdriver.Ie()
#     elif browser_type == "FF":
#         driver = webdriver.Firefox()
#     else:
#         driver = webdriver.Chrome()
#     return driver

class BasePage:

    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    def loc(self, loc):
        return self.driver.find_element(*loc)


    def visit(self):
        self.driver.get(self.url)

    def wait(self,time):
        self.driver.implicitly_wait(time)

    def quit_browser(self):
        self.driver.quit()