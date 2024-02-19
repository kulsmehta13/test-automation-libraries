import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium_lib.selenium_lib import SeleniumLib


class TestSeleniumLib(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = SeleniumLib("chrome")
        cls.selenium.connect()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.close()

    def test_navigation(self):
        self.selenium.navigate_to("https://the-internet.herokuapp.com/")
        self.assertIn("Example Domain", self.selenium.driver.title)

    def test_element_visibility(self):
        locator = (By.ID, "checkboxes")
        element = self.selenium.wait_for_element_visibility(locator)
        self.assertTrue(element.is_displayed())

    def test_find_element(self):
        element = self.selenium.find_element(By.NAME, "username")
        self.assertIsNotNone(element)

    def test_click_element(self):
        element = self.selenium.find_element(By.XPATH, "//button[contains(text(),'Click me')]")
        self.selenium.click_element(element)
        # Add assertions based on the expected behavior after clicking the element

    def test_send_keys_to_element(self):
        element = self.selenium.find_element(By.CSS_SELECTOR, "input[type='text']")
        text_to_send = "Test Input"
        self.selenium.send_keys_to_element(element, text_to_send)
        self.assertEqual(element.get_attribute("value"), text_to_send)


if __name__ == '__main__':
    unittest.main()
