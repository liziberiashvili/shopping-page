from selenium import webdriver


class BrowserFactory:
    @staticmethod
    def get_browser(browser="firefox"):
        if browser.lower() == "chrome":
            return webdriver.Chrome()
        elif browser == "firefox":
            return webdriver.Firefox()
        elif browser == "Safari":
            return webdriver.Safari()
