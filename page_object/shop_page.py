from base_page.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from log.log import Logger

class Shop(BasePage):
    url = "http://39.98.138.157/shopxo/index.php?s=/index/search/index"
    shop1 = (By.XPATH,'/html/body/div[4]/div/ul/li[1]/div/a/img')


    def click_shop1(self):
        self.loc(self.shop1).click()

    def click_shop(self):
        self.visit()
        self.loc(self.shop1).click()
        sleep(3)