from base_page.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from log.log import Logger
class LoginPage(BasePage):
    #页面url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
    #页面元素
    uname = (By.NAME, "accounts")

    upwd = (By.NAME, "pwd")

    loginbt = (By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button")

    #页面操作
    def input_uname(self,txt):
        self.loc(self.uname).send_keys(txt)

    def input_upwd(self,txt):
        self.loc(self.upwd).send_keys(txt)

    def click_loginbt(self):
        self.loc(self.loginbt).click()

    #登录流程
    def login(self, username, password):
        self.visit()
        self.input_uname(username)
        self.input_upwd(password)
        self.click_loginbt()
        sleep(10)

    def assert_text(self,loc_type,value,expect):
        try:
            reality = self.driver.find_element(getattr(By,loc_type.upper()),value).text
            assert reality == expect
            Logger().log().info("登录流程正确，断言成功！")
            return True
        except Exception as e:
            Logger().log().info("登录流程正确，断言失败！")
            return False

