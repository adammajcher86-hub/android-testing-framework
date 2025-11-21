"""
Factory for creating and managing Appium driver instances
"""

import logging
from appium import webdriver
from config.capabilities import APPIUM_SERVER, get_capabilities

logger = logging.getLogger(__name__)


class DriverFactory:
    """Factory class for creating Appium WebDriver instances"""

    _driver = None

    @classmethod
    def get_driver(cls):
        """
        Get or create Appium WebDriver instance

        Returns:
            WebDriver: Appium WebDriver instance
        """
        if cls._driver is None:
            capabilities = get_capabilities()

            logger.info("Creating new driver with capabilities")
            cls._driver = webdriver.Remote(APPIUM_SERVER, options=capabilities)
            logger.info("Driver created successfully")

        return cls._driver

    @classmethod
    def quit_driver(cls):
        """Quit and cleanup driver instance"""
        if cls._driver is not None:
            logger.info("Quitting driver")
            cls._driver.quit()
            cls._driver = None
