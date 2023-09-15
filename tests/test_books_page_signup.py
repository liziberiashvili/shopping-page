from steps.books_page_signup_steps import BooksPageSignupSteps


class TestBooksPageSignup:
    def test_sign_up(self):
        BooksPageSignupSteps.fill_user_fields()
