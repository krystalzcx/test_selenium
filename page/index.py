# 非登录首页
from selenium.webdriver.common.by import By
from page.register import Register


class Index:
    # 简陋初始化driver
    def __init__(self, driver):
        self.driver = driver

    def goto_register(self):
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        # 进入另一个页面，需要return
        return Register(self.driver)
