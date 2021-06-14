# 非登录首页
from selenium.webdriver.common.by import By
from page.register import Register
from page.base_page import BasePage
from page.login import Login


class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    #跳转到注册页
    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, "立即注册").click()
        # 进入另一个页面，需要return
        return Register(self._driver)

    #跳转到登录页
    def goto_login(self):
        self._driver.find_element(By.LINK_TEXT, "企业登录").click()
        #此处必须传递driver参数，否则会报无_base_url的错误，实际也是在说无driver
        return Login(self._driver)
