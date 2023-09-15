import time

from pages.shopping_home_page import ShoppingHomePage
from steps.shopping_page_steps import ShoppingPageSteps


class TestShoppingPage:
    username = "standard_user"
    password = "secret_sauce"

    def test_shopping(self):
        ShoppingPageSteps.login(self.username, self.password)


        shopping_home_page = ShoppingHomePage()
        assert shopping_home_page.find_home_page_logo(), "authorization failed"

        shopping_home_page.add_backpack_to_cart()
        shopping_home_page.add_bike_light_to_cart()
        assert shopping_home_page.get_text_from_cart_badge() == "2", "adding_items_to_the_cart has failed"



