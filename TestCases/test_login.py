from Pages import Login
import pytest
from Library.ConfigReader import read_config_data



def get_valid_credentials():
    valid_usernames = read_config_data("Login", "valid_usernames").split()
    return valid_usernames

@pytest.mark.parametrize("data", get_valid_credentials())
def test_valid_login(data, setup):
    login = Login.LoginPage(setup)
    login.enter_username(data)
    valid_password = read_config_data("Login", "valid_password")
    login.enter_password(valid_password)
    login.click_login_button()

    plp_url = read_config_data("PLP", "PLP_URL")
    assert plp_url == setup.current_url


def test_invalid_login_empty_username(setup):
    login = Login.LoginPage(setup)
    invalid_password = read_config_data("Login", "invalid_password")
    login.enter_password(invalid_password)
    login.click_login_button()
    error_message_empty_username  = read_config_data("Login", "error_message_empty_username")

    current_error_message = login.get_error_message()
    assert current_error_message == error_message_empty_username


def test_invalid_login_empty_password(setup):
    login = Login.LoginPage(setup)
    invalid_username = read_config_data("Login", "invalid_username")
    login.enter_username(invalid_username)
    login.click_login_button()

    error_message_empty_password = read_config_data("Login", "error_message_empty_password")
    current_error_message = login.get_error_message()
    assert current_error_message == error_message_empty_password

def test_invalid_login_data_filled(setup):
    login = Login.LoginPage(setup)
    invalid_username = read_config_data("Login", "invalid_username")
    invalid_password = read_config_data("Login", "invalid_password")
    login.enter_username(invalid_username)
    login.enter_password(invalid_password)
    login.click_login_button()

    current_error_message = login.get_error_message()
    error_message_incorrect_credentials = read_config_data("Login", "error_message_incorrect_credentials")
    assert current_error_message == error_message_incorrect_credentials


def test_invalid_login_locked_out_user(setup):
    login = Login.LoginPage(setup)
    locked_out_username = read_config_data("Login", "locked_out_username")
    valid_password = read_config_data("Login", "valid_password")
    login.enter_username(locked_out_username)
    login.enter_password(valid_password)
    login.click_login_button()

    current_error_message = login.get_error_message()
    error_message_locked_out = read_config_data("Login", "error_message_locked_out")
    assert current_error_message == error_message_locked_out