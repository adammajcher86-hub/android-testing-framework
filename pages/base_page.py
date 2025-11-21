"""
Base Page - Parent class for all page objects
Contains common methods used by all pages
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base class for all page objects"""

    def __init__(self, driver):
        """
        Initialize page with driver

        Args:
            driver: Appium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

    def find_element(self, locator):
        """
        Find element with explicit wait

        Args:
            locator: Tuple of (By, value) - e.g., (AppiumBy.ID, 'element_id')

        Returns:
            WebElement: Found element
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """
        Click element with explicit wait

        Args:
            locator: Tuple of (By, value)
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text):
        """
        Type text into element

        Args:
            locator: Tuple of (By, value)
            text: Text to type
        """
        element = self.find_element(locator)
        element.clear()  # Clear existing text first
        element.send_keys(text)

    def is_displayed(self, locator):
        """
        Check if element is visible

        Args:
            locator: Tuple of (By, value)

        Returns:
            bool: True if visible, False otherwise
        """
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except Exception as e:
            print(f"ℹElement is not visible, error: {e}")
            return False

    def get_text(self, locator):
        """
        Get text from element

        Args:
            locator: Tuple of (By, value)

        Returns:
            str: Element text
        """
        element = self.find_element(locator)
        return element.text

    def wait_for_element(self, locator, timeout=10):
        """
        Wait for element to appear

        Args:
            locator: Tuple of (By, value)
            timeout: Max seconds to wait

        Returns:
            WebElement: Found element
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))
