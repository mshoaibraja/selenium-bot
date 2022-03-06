import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers",
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_elements(by=By.CSS_SELECTOR,
                                               value='button[data-tooltip-text="Choose your currency"]')[0]
        currency_element.click()
        selected_currency_element = self.find_elements(by=By.CSS_SELECTOR,
                                                       value=f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')[0]
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_elements(By.ID, value='ss')[0]
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_elements(By.CSS_SELECTOR, value='li[data-i="0"]')[0]
        first_result.click()
