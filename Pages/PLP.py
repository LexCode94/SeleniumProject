from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec



class PLP:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 100)
        self.select_element = (By.XPATH, '//select[@class="product_sort_container"]')
        self.product_names_elements = (By.XPATH, '//div[@class="inventory_item_name "]')
        self.product_prices_elements = (By.XPATH, '//div[@class="inventory_item_price"]')
        self.add_buttons = (By.XPATH, '//button[@class="btn btn_primary btn_small btn_inventory "]')
        self.remove_buttons = (By.XPATH, '//button[@class="btn btn_secondary btn_small btn_inventory "]')
        self.number_of_cart_items = (By.XPATH,'//span[@class="shopping_cart_badge"]')

    def sort(self, value):

        dropdown = self.wait.until(ec.element_to_be_clickable(self.select_element))
        select = Select(dropdown)
        select.select_by_value(value)

    def get_product_names(self):
        product_names = self.wait.until(ec.presence_of_all_elements_located(self.product_names_elements))
        product_names_text = []

        for i in range(0, len(product_names)):
            product_names_text.append( product_names[i].text)

        return product_names_text

    def get_product_prices(self):
        product_prices = self.wait.until(ec.presence_of_all_elements_located(self.product_prices_elements))
        product_prices_numbers = []

        for i in range(0, len(product_prices)):
            product_prices_numbers.append(product_prices[i].text)

        product_prices_float = []

        for p in product_prices_numbers:
            clean_price = p.replace("$", "")
            product_prices_float.append(float(clean_price))

        return product_prices_float


    def click_add_buttons(self, number):
        all_add_buttons = self.wait.until(ec.presence_of_all_elements_located(self.add_buttons))

        num = number
        for button in all_add_buttons:
            button.click()
            num-=1
            if num <= 0:
                break


    def get_remove_buttons(self):
        all_remove_buttons = self.wait.until(ec.presence_of_all_elements_located(self.remove_buttons))

        return len(all_remove_buttons)

    def click_remove_buttons(self, number):
        all_remove_buttons = self.wait.until(ec.presence_of_all_elements_located(self.remove_buttons))
        num = number
        for button in all_remove_buttons:
            button.click()
            num-=1
            if num <= 0:
                break
                

    def get_number_of_items_in_cart(self):
        cart_items = self.wait.until(ec.visibility_of_element_located(self.number_of_cart_items))
        return int(cart_items.text)