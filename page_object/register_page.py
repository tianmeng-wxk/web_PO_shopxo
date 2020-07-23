from base_page.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from log.log import Logger
class Register(BasePage):
    url = "http://39.98.138.157/shopxo/index.php?s=/index/user/reginfo.html"

    uname = (By.NAME,'accounts')
    upwd = (By.NAME, 'pwd')
    read = (By.XPATH,'/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[3]/label/span')
    registerbt = (By.XPATH,'/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[4]/button')

    def input_uname(self,txt):
        self.loc(self.uname).send_keys(txt)

    def input_upwd(self,txt):
        self.loc(self.upwd).send_keys(txt)

    def click_read(self):
        self.loc(self.read).click()

    def click_registerbt(self):
        self.loc(self.registerbt).click()


    def register(self,username,password):
        self.visit()
        self.input_uname(username)
        self.input_upwd(password)
        self.click_read()
        self.click_registerbt()

    def assert_text(self,loc_type,value,expect):
        try:
            reality = self.driver.find_element(getattr(By,loc_type.upper()),value).text
            assert reality == expect
            Logger().log().info("注册流程正确，断言成功！")
            return True
        except Exception as e:
            Logger().log().info("注册流程正确，断言失败！")
            return False
