import time

from faker import Faker

from data.models.books_page_user import BooksPageUser
from managers.DriverManager import DriverManager
from pages.books_page_signup import BooksPageSignup
from utils.RandomUtils import RandomUtils

fake = Faker()
firstname = fake.first_name()
lastname = fake.last_name()
username = fake.user_name()
password = RandomUtils.books_page_password()


class BooksPageSignupSteps:
    @staticmethod
    def fill_user_fields():
        user = BooksPageUser(firstname, lastname, username, password)
        books_page_signup = BooksPageSignup()
        books_page_signup.click_new_user()
        time.sleep(5)
        books_page_signup.fill_first_name(user.firstname)
        books_page_signup.fill_last_name(user.lastname)
        books_page_signup.fill_username(user.username)
        books_page_signup.fill_password(user.password)
        books_page_signup.switch_to_iframe()
        books_page_signup.recaptcha_handler()
        time.sleep(5)
        books_page_signup.click_register()
        books_page_signup.click_login()
