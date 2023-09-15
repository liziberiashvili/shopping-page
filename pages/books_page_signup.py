from selenium.webdriver.common.by import By

from elements.button import Button
from elements.element import Element
from elements.input import Input
from utils.DriverUtils import DriverUtils


class BooksPageSignup:
    __new_user = Button(By.XPATH, "//button[@id='newUser']", "new_user")
    __first_name = Input(By.XPATH, "//input[@id='firstname']", "first_name")
    __last_name = Input(By.XPATH, "//input[@id='lastname']", "last_name")
    __username = Input(By.XPATH, "//input[@id='userName']", "username")
    __password = Input(By.XPATH, "//input[@id='password']", "password")
    __iframe = Element(By.XPATH, "//iframe[@title='reCAPTCHA']", "iframe")
    __recaptcha_checkbox = Button(By.XPATH, "//div[@class='recaptcha-checkbox-border']", "recaptcha")
    __register = Button(By.XPATH, "//button[@id='register']", "register")
    __login = Button(By.XPATH, "//div[@class='element-list collapse show']//li[@id='item-0']", "login")

    def click_new_user(self):
        self.__new_user.click()

    def fill_first_name(self, firstname):
        self.__first_name.send_text(firstname)

    def fill_last_name(self, lastname):
        self.__last_name.send_text(lastname)

    def fill_username(self, username):
        self.__username.send_text(username)

    def fill_password(self, password):
        self.__password.send_text(password)

    def switch_to_iframe(self):
        DriverUtils.switch_to_iframe(self.__iframe)

    def recaptcha_handler(self):
        self.__recaptcha_checkbox.click()

    def click_register(self):
        self.__register.click()

    def click_login(self):
        self.__login.click()
