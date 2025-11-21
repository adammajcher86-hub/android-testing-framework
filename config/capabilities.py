"""
Appium capabilities configuration for Android testing
"""

import os
from appium.options.android import UiAutomator2Options

# Project paths
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_PATH = os.path.join(PROJECT_ROOT, "apps", "wikipedia.apk")

# Appium server URL
APPIUM_SERVER = "http://127.0.0.1:4723"

# App details
APP_PACKAGE = "org.wikipedia"
APP_ACTIVITY = "org.wikipedia.main.MainActivity"


def get_capabilities():
    """
    Get Android emulator capabilities (CI-ready)

    This configuration works for:
    - Local development (your emulator)
    - GitHub Actions CI/CD (cloud emulator)

    Returns:
        UiAutomator2Options: Configured capabilities
    """
    options = UiAutomator2Options()

    # Platform settings
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"

    # App settings
    options.app = APP_PATH
    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY

    # Test settings
    options.no_reset = False  # Clear app data before each test
    options.full_reset = False  # Don't uninstall app
    options.new_command_timeout = 300  # 5 minutes timeout

    # Performance settings
    options.auto_grant_permissions = True  # Auto-grant app permissions
    options.disable_window_animation = True  # Faster test execution

    return options
