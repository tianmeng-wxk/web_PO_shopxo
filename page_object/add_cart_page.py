from base_page.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from log.log import Logger
from selenium.webdriver.support.ui import WebDriverWait
class AddCart(BasePage):
    url = "http://39.98.138.157/shopxo/index.php?s=/index/goods/index/id/2.html"

    set_mean2 = (By.XPATH,'/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[1]/ul/li[2]')
    color2 = (By.XPATH,'/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[2]/ul/li[2]')
    capacity2 = (By.XPATH,'/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[3]/ul/li[2]')
    add_cartbt = (By.XPATH,'/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/button')
    cart = (By.XPATH,"/html/body/div[1]/div/ul[2]/div[4]/div/a/span")
    sum = (By.XPATH,'/html/body/div[2]/div/ul[2]/div[4]/div/a/strong')
    all_check = (By.XPATH,'/html/body/div[5]/div/div[1]/label/span[1]/i[2]')
    clear = (By.XPATH,'/html/body/div[5]/div/div[1]/a')
    sure = (By.XPATH,'//*[@id="am-modal-rfrr0"]/div/div[3]/span[2]')
    shop_sum = (By.XPATH,'//*[@id="data-list-528"]/td[3]/div/input')

    def click_mean(self):
        self.loc(self.set_mean2).click()
    def click_color(self):
        self.loc(self.color2).click()
    def click_capacity(self):
        self.loc(self.capacity2).click()
    def click_add_cartbt(self):
        self.loc(self.add_cartbt).click()
    def click_cart(self):
        self.loc(self.cart).click()

    def click_all_check(self):
        self.loc(self.all_check).click()
    def click_clear(self):
        self.loc(self.clear).click()
    def click_sure(self):
        self.loc(self.sure).click()



    def add_shop_cart(self):
        self.visit()
        self.click_mean()
        sleep(1)
        self.click_color()
        sleep(1)
        self.click_capacity()
        sleep(1)
        self.click_add_cartbt()

    def assert_text(self, loc_type, value, expect):
        try:
            reality = self.driver.find_element(getattr(By, loc_type.upper()), value)
            assert reality == expect
            Logger().log().info("加入购物车流程正确，断言成功！")
            return True
        except Exception as e:
            Logger().log().info("加入购物车流程正确，断言失败！")
            return False