from selenium.webdriver.common.by import By

from elements.button import Button
from elements.input import Input


class LoginPage:
    __username = Input(By.XPATH, "//input[@id='user-name']", "username")
    __password = Input(By.XPATH, "//input[@id='password']", "password")
    __login = Button(By.XPATH, "//input[@id='login-button']", "login")

    def fill_username(self, username):
        self.__username.send_text(username)

    def fill_password(self, password):
        self.__password.send_text(password)

    def click_login(self):
        self.__login.click()
