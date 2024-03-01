from pageObjects.LoginPage import LoginClass


class Test_UserLogin:


    def test_Verify_Url_001(self, setup):
        self.driver = setup
        Page_Title = self.driver.title
        print(Page_Title)
        if Page_Title == "OrangeHRM":
            assert True
        else:
            assert False


    def test_User_Login_002(self, setup):
        self.driver = setup
        self.lp = LoginClass(self.driver)
        self.lp.Enter_UserName("Admin")
        self.lp.Enter_Password("admin123")
        self.lp.Click_Login_Button()
        self.lp.Click_Menu_Button()
        self.lp.Click_Logout_Button()
