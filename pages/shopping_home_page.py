from selenium.webdriver.common.by import By

from elements.button import Button
from elements.element import Element


class ShoppingHomePage:
    __home_page_logo = Element(By.XPATH, "//div[@class='app_logo']", "home_page_logo")
    __backpack_add_cart_button = Button(By.XPATH, "//button[@data-test = 'add-to-cart-sauce-labs-backpack']",
                                        "backpack")
    __bike_light_add_cart_button = Button(By.XPATH, "//button[@data-test = 'add-to-cart-sauce-labs-bike-light']",
                                          "bike-light")
    __shopping_cart_badge = Button(By.XPATH, "//span[@class='shopping_cart_badge']",
                                   "shopping_cart_padge")

    def find_home_page_logo(self):
        return self.__home_page_logo.is_visible()

    def add_backpack_to_cart(self):
        self.__backpack_add_cart_button.click()

    def add_bike_light_to_cart(self):
        self.__bike_light_add_cart_button.click()

    def get_text_from_cart_badge(self):
        return self.__shopping_cart_badge.get_text()
