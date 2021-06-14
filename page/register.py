from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Register(BasePage):
    def register(self, corpname):
        self._driver.find_element(By.ID, "corp_name").send_keys("霍格沃兹测试学院")
        self._driver.find_element(By.ID, "submit_btn").click()
        # 注册结束，返回对象
        # 当前写的都是注册失败的，所以返回的是自己
        return self

    #  断言返回的   
    def get_error_message(self):
        # 原定位符可以定位多个的
        # result = []
        # for element in self._driver.find_elements(By.CSS_SELECTOR, '.js_corp_industry_text'):
        #     result.append(element.text)
        # return result
        # 现在的定位符可以定位到唯一的
        return self._driver.find_element(By.CSS_SELECTOR, '.js_corp_industry_text').text
        