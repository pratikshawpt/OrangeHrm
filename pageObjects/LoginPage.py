from selenium.webdriver.common.by import By


class LoginClass:
    Text_Username_Xpath = "//input[@placeholder='Username']"
    Text_Password_Xpath = "//input[@placeholder='Password']"
    Click_LoginButton_Xpath = "//button[@type='submit']"
    Click_MenuButton_Xpath = "//p[@class='oxd-userdropdown-name']"
    Click_Logout_Xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def Enter_UserName(self, username):
        self.driver.find_element(By.XPATH, self.Text_Username_Xpath).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(By.XPATH, self.Text_Password_Xpath).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(By.XPATH, self.Click_LoginButton_Xpath).click()

    def Click_Menu_Button(self):
        self.driver.find_element(By.XPATH, self.Click_MenuButton_Xpath).click()

    def Click_Logout_Button(self):
        self.driver.find_element(By.XPATH, self.Click_Logout_Xpath).click()
