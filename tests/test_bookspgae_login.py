import time

import requests

from managers.DriverManager import DriverManager
from steps.books_page_login import BooksPageLoginSteps


class TestBooksPageLogin:
    def test_login(self):
        username = "test1234"
        password = "Test1234@"
        BooksPageLoginSteps.login(username, password)
        time.sleep(5)

        all_cookies = DriverManager.get_driver().get_cookies()
        print(all_cookies)
        body = {
            "userName": username,
            "password": password
        }
        generate_token = requests.post("https://demoqa.com/Account/v1/GenerateToken",
                                       json=body)
        assert generate_token.status_code == 200
        token = generate_token.json()["token"]
        print(token)

        userID = ""
        for i in all_cookies:
            if i.get('name') == 'userID':
                userID = i.get('value')
        json = {
            "UUID": userID
        }

        header = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.get("https://demoqa.com/Account/v1/User/{UUID}", headers=header, params=json)
        print(userID)
        print(response.text)
