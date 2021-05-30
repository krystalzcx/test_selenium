from page.main import Main


class TestMain:

    def test_add_member(self):
        main = Main()
        main.add_member().add_member("xxx")