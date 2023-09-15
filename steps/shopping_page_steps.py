from pages.shopping_home_page import ShoppingHomePage
from pages.shopping_login_page import LoginPage


class ShoppingPageSteps:
    @staticmethod
    def login(username, password):
        login_page = LoginPage()
        login_page.fill_username(username)
        login_page.fill_password(password)
        login_page.click_login()






