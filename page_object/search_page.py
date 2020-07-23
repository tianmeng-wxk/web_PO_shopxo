from base_page.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from log.log import Logger

class SearchPage(BasePage):
    #url
    url = 'http://39.98.138.157/shopxo/index.php'

    #页面元素
    search = (By.XPATH,'//*[@id="search-input"]')
    searchbt = (By.XPATH,'//*[@id="ai-topsearch"]')

    #元素操作
    def input_search(self,txt):
        self.loc(self.search).send_keys(txt)

    def click_searchbt(self):
        self.loc(self.searchbt).click()


    #搜索流程
    def search_shop(self,txt):
        self.visit()
        self.input_search(txt)
        self.click_searchbt()
        sleep(5)

    #断言方法
    def assert_text(self,loc_type,value,expect):
        try:
            #获取到总的搜索内容
            items = self.driver.find_elements(getattr(By,loc_type.upper()),value)
            print(items)
            reality = []
            #遍历出一个个商品的内容
            for itme in items:
                reality.append(itme.text)
            Logger().log().info("搜索出的商品列表：", reality)
            assert expect in reality
            Logger().log().info("搜索流程正确，断言成功！")
            return True
        except Exception as e:
            Logger().log().info("搜索流程正确，断言失败！")
            return False


