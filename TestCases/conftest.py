from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import pytest

from Pages import Login
from Library.ConfigReader import read_config_data


@pytest.fixture
def setup():
    service1 = Service(executable_path="../Driver/chromedriver.exe")
    driver = Chrome(service=service1)
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login(setup):
    login = Login.LoginPage(setup)
    valid_usernames = read_config_data("Login", "valid_usernames").split()
    valid_username = valid_usernames[0]
    valid_password = read_config_data("Login", "valid_password")
    login.enter_username(valid_username)
    login.enter_password(valid_password)
    login.click_login_button()
    return login
