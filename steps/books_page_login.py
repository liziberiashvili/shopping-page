from pages.books_page_login import BooksPageLogin


class BooksPageLoginSteps:
    @staticmethod
    def login(username, password):
        books_page_login = BooksPageLogin()
        books_page_login.fill_user_name(username)
        books_page_login.fill_password(password)
        books_page_login.click_button_login()