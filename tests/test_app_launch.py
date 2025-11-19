"""
Basic tests for Wikipedia app launch and initial setup
"""
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy


class TestAppLaunch:
    """Test suite for app launch scenarios"""
    
    @pytest.mark.smoke
    def test_app_launches_successfully(self, driver):
        """
        Test that Wikipedia app launches successfully
        
        Steps:
        1. App launches
        2. Wait for app to load
        3. Verify app is running
        """
        # App should launch automatically with our capabilities
        time.sleep(3)  # Wait for app to fully load
        
        # Get current activity to verify app launched
        current_activity = driver.current_activity
        current_package = driver.current_package

        print(f"Current package: {current_package}")
        print(f"Current activity: {current_activity}")

        # Wikipedia app can launch to either onboarding or main activity
        assert current_package == 'org.wikipedia', \
            f"Expected org.wikipedia, got: {current_package}"

        # Accept either onboarding or main activity
        assert 'wikipedia' in current_package.lower(), \
            f"Expected Wikipedia app, got: {current_package}"

        print("✓ Wikipedia app launched successfully")

    @pytest.mark.smoke
    def test_skip_onboarding(self, driver):
        """
        Test skipping the initial onboarding screens

        Steps:
        1. App launches with onboarding
        2. Skip onboarding
        3. Verify main screen is displayed
        """
        time.sleep(2)

        try:
            # Look for Skip button (onboarding might appear on first launch)
            skip_button = driver.find_element(
                AppiumBy.ID,
                'org.wikipedia:id/fragment_onboarding_skip_button'
            )
            skip_button.click()
            print("✓ Clicked Skip button")
            time.sleep(1)
        except:
            print("ℹ No onboarding screen (already skipped or not shown)")

        # Verify we're on the main screen by looking for search bar
        try:
            search_container = driver.find_element(
                AppiumBy.ID,
                'org.wikipedia:id/search_container'
            )
            assert search_container.is_displayed(), "Search container not visible"
            print("✓ Main screen displayed successfully")
        except Exception as e:
            pytest.fail(f"Failed to find main screen elements: {e}")

    def test_app_package_and_activity(self, driver):
        """
        Verify app package is correct (activity may vary on first launch)
        """
        current_package = driver.current_package
        current_activity = driver.current_activity

        print(f"Package: {current_package}")
        print(f"Activity: {current_activity}")

        # Check package is correct
        assert current_package == 'org.wikipedia', \
            f"Expected org.wikipedia, got {current_package}"

        # Activity can be MainActivity OR InitialOnboardingActivity - both are valid
        valid_activities = ['MainActivity', 'InitialOnboardingActivity', 'OnboardingActivity']
        activity_is_valid = any(activity in current_activity for activity in valid_activities)

        assert activity_is_valid, \
            f"Expected Wikipedia activity (MainActivity or Onboarding), got {current_activity}"

        print(f"✓ App package correct: {current_package}")
        print(f"✓ Activity valid: {current_activity}")