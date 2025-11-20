"""
Search functionality tests
"""
import pytest
from pages.home_page import HomePage
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class TestSearch:
    """Test suite for Wikipedia search functionality"""
    SEARCH_INPUT = (AppiumBy.ID, 'org.wikipedia:id/search_src_text')
    SEARCH_RESULTS_LIST = (AppiumBy.ID, 'org.wikipedia:id/search_results_list')

    @pytest.mark.smoke
    def test_search_box_is_displayed(self, driver):
        """
        Test that search box is visible on home page

        Steps:
        1. Launch app
        2. Skip onboarding if present
        3. Verify search box is displayed
        """
        # Arrange - Create page object
        home_page = HomePage(driver)

        # Act - Skip onboarding
        home_page.skip_onboarding()

        # Assert - Verify search is visible
        assert home_page.is_search_displayed(), "Search box should be visible"
        print("✓ Test passed: Search box is displayed")

    @pytest.mark.search
    def test_search_opens_search_screen(self, driver):
        """
        Test that clicking search box opens search screen

        Steps:
        1. Launch app
        2. Skip onboarding
        3. Click search box
        4. Verify search input field appears
        """
        # Arrange
        home_page = HomePage(driver)
        home_page.skip_onboarding()

        # Act - Click search
        search_page = home_page.click_search_box()

        # Assert - Verify search input is displayed
        assert search_page.is_search_input_displayed(), \
            "Search input field should be visible"
        print("✓ Test passed: Search screen opened")

    @pytest.mark.search
    def test_search_returns_results(self, driver):
        """Test that searching displays results list"""
        home_page = HomePage(driver)
        home_page.skip_onboarding()

        search_page = home_page.click_search_box()
        search_page.enter_search_text("Python programming")

        # Just check list appears
        assert search_page.is_results_displayed(), \
            "Search results should be displayed"

        print("✓ Test passed: Search results displayed")


    @pytest.mark.search
    def test_search_result_contains_search_term(self, driver):
        """
        Test that searching returns relevant results

        Steps:
        1. Launch app
        2. Skip onboarding
        3. Search for "Python programming"
        4. Verify results are displayed
        5. Verify first result contains "Python"
        """
        # Arrange
        home_page = HomePage(driver)
        home_page.skip_onboarding()

        # Act - Perform search
        search_page = home_page.click_search_box()
        search_page.enter_search_text("Python programming")

        # Assert 1 - Results are displayed
        assert search_page.is_results_displayed(), \
            "Search results should be displayed"

        # Assert 2 - First result is relevant
        first_result_text = search_page.get_first_result_text()
        print(f"First result: {first_result_text}")

        assert "python" in first_result_text.lower(), \
            f"First result should contain 'Python', got: {first_result_text}"

        print("✓ Test passed: Search returned relevant results")