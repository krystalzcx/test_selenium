# 对通用代码封装
from selenium import webdriver
from selenium.webdriver.remote.webdriver  import WebDriver
import time

class BasePage:
    def __init__(self, driver: WebDriver=None):
        if driver is None:
            # index页面使用这个方法
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
            self._driver.get(self._base_url)       
        else:
            # 是因为有的页面需要引用其他的driver
            # login和register等页面需要这个方法
            self._driver = driver

    def close(self):
        time.sleep(20)
        self._driver.quit()