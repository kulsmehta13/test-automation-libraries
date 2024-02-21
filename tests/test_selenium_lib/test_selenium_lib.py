import unittest
from unittest.mock import patch,MagicMock
from test_automation_libraries.selenium_lib.selenium_lib import SeleniumLib

class TestSeleniumLib(unittest.TestCase):
    def setUp(self):
        self.selenium_lib = SeleniumLib('chrome')

    def tearDown(self):
        pass

    def test_connect(self):
        # Mock the webdriver and assert that the connect method is called
        with patch('test_automation_libraries.selenium_lib.selenium_lib.webdriver') as mock_webdriver:
            self.selenium_lib.connect()
            mock_webdriver.Chrome.assert_called_once()

    @patch('test_automation_libraries.selenium_lib.selenium_lib.logging')
    def test_close(self, mock_logging):
        # Create a mock driver with a quit method
        mock_driver = MagicMock()
        mock_driver.quit = MagicMock()

        # Instantiate SeleniumLib and set its driver to the mock driver
        self.selenium_lib.driver = mock_driver

        # Call the close method
        self.selenium_lib.close()

        # Assert that the driver's quit method was called
        mock_driver.quit.assert_called_once()
    
    @patch('test_automation_libraries.selenium_lib.selenium_lib.logging')
    def test_close_with_exception(self, mock_logging):
        # Create a mock driver with a quit method that raises an exception
        mock_driver = MagicMock()
        mock_driver.quit = MagicMock(side_effect=Exception('Test exception'))

        # Instantiate SeleniumLib and set its driver to the mock driver
        self.selenium_lib.driver = mock_driver

        # Assert that an exception is raised when calling the close method
        with self.assertRaises(Exception):
            self.selenium_lib.close()

        # Assert that the error was logged twice
        self.assertEqual(mock_logging.error.call_count, 2)
        mock_logging.error.assert_called_with('Error occurred during browser closing: Test exception')

    @patch('test_automation_libraries.selenium_lib.selenium_lib.logging')
    def test_navigate_to(self, mock_logging):
        # Create a mock driver with a get method
        mock_driver = MagicMock()
        mock_driver.get = MagicMock()

        # Instantiate SeleniumLib and set its driver to the mock driver
        self.selenium_lib.driver = mock_driver

        # Call the navigate_to method
        self.selenium_lib.navigate_to('http://testurl.com')

        # Assert that the driver's get method was called with the correct URL
        mock_driver.get.assert_called_once_with('http://testurl.com')

    @patch('test_automation_libraries.selenium_lib.selenium_lib.logging')
    def test_navigate_to_with_exception(self, mock_logging):
        # Create a mock driver with a get method that raises an exception
        mock_driver = MagicMock()
        mock_driver.get = MagicMock(side_effect=Exception('Test exception'))

        # Instantiate SeleniumLib and set its driver to the mock driver
        
        self.selenium_lib.driver = mock_driver

        # Assert that an exception is raised when calling the navigate_to method
        with self.assertRaises(Exception):
            self.selenium_lib.navigate_to('http://testurl.com')

        # Assert that the error was logged twice (due to the retry decorator)
        self.assertEqual(mock_logging.error.call_count, 2)
        mock_logging.error.assert_called_with('Error occurred during navigation: Test exception')