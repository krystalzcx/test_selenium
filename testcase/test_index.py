import sys
sys.path.append(r"D:\worksapce\test_selenium")
from page.index import Index

class TestIndex:
    def setup(self):
        self.index = Index()

    def test_register(self):
        # 链式调用：两个类中方法连续调用
        self.index.goto_register().register("霍格沃兹学院")
    
    def test_login(self):
        # register_page是因为最终调用的register()方法也是返回的自己
        register_page = self.index.goto_login().goto_registry().register("测试（北京）科技有限公司")
        print(register_page.get_error_message())
        # assert "请选择" in  "|".join(register_page.get_error_message())
        assert "选择" in register_page.get_error_message()

    def teardown(self):
        self.index.close()