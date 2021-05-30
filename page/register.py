from selenium.webdriver.common.by import By


class Register:
    # 简陋初始化driver
    def __init__(self, driver):
        self.driver = driver

    def register(self, corpname):
        self.driver.find_element(By.ID, "corp_name").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, "submit_btn").click()
        