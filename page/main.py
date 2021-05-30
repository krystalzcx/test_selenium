from page.contact import Contact


# 企业微信首页
class Main():
    def download(self):
        pass

    def import_user(self):
        return self

    def goto_app(self):
        pass

    def goto_compay(self):
        pass
    
    # 不是所有方法都需要返回PO对象，获取信息这个功能就会真实获得一个列表
    def get_message(self):
        return ["aaa", "bbbzxghio"]

    # 首页上的按钮只是一个跳转，跳转到新PO(返回其他PO对象)
    def add_member(self):
        return Contact()



