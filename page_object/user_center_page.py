from base_page.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
class UserCenterPage(BasePage):
    #页面url
    url = "http://39.98.138.157/shopxo/index.php?s=/index/user/index.html"
    #页面元素
    orderbt = (By.XPATH,'//*[@id="collapse-nav-business"]/li[1]/a')
    search = (By.XPATH,"/html/body/div[4]/div[3]/div/form/div/div/input")
    searchbt = (By.XPATH,"/html/body/div[4]/div[3]/div/form/div/div/span/button")

    #元素操作
    def click_orderbt(self):
        self.loc(self.orderbt).click()

    def input_search(self,txt):
        self.loc(self.search).send_keys(txt)

    def click_searchbt(self):
        self.loc(self.searchbt).click()

    #搜索订单号流程
    def search_infor(self, txt):
        self.visit()
        self.click_orderbt()
        self.input_search(txt)
        self.click_searchbt()


