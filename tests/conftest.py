import pytest

from managers.DriverManager import DriverManager
from utils.ParserUtils import ParserUtils


@pytest.fixture(autouse=True, scope="function")
def setUp():
    config_data = ParserUtils.parse_json("../resources/config.json")
    driver = DriverManager.get_driver()
    driver.get(config_data["url"])
    driver.maximize_window()
    yield
    DriverManager.close_driver()
