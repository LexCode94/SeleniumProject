from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.username_field = (By.XPATH, '//input[@id="user-name" and @placeholder="Username"]')
        self.password_field = (By.XPATH, '//input[@id="password" and @placeholder="Password"]')
        self.login_button = (By.XPATH, '//input[@id="login-button" and @value="Login"]')
        self.error_messages_container = (By.XPATH, '//div[@class="error-message-container error"]/child::h3')

    def enter_username(self, username):
        self.wait.until(ec.element_to_be_clickable(self.username_field)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(ec.element_to_be_clickable(self.password_field)).send_keys(password)

    def click_login_button(self):
        self.wait.until(ec.element_to_be_clickable(self.login_button)).click()

    def get_error_message(self):
        return self.wait.until(ec.visibility_of_element_located(self.error_messages_container)).text