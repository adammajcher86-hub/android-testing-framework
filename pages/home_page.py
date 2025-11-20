
"""
Home Page - Wikipedia main screen
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.search_page import SearchPage

class HomePage(BasePage):
    """Wikipedia home page object"""

    # LOCATORS - All element identifiers in one place
    SKIP_BUTTON = (AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')
    SEARCH_CONTAINER = (AppiumBy.ID, 'org.wikipedia:id/search_container')
    SEARCH_TEXT = (AppiumBy.ID, 'org.wikipedia:id/search_src_text')

    # ACTIONS - What you can DO on this page

    def skip_onboarding(self):
        """
        Skip onboarding screens if they appear

        Returns:
            HomePage: Self for method chaining
        """
        try:
            self.click(self.SKIP_BUTTON)
            print("✓ Skipped onboarding")
        except:
            print("ℹ No onboarding screen")
        return self

    def is_search_displayed(self):
        """
        Check if search box is visible (confirms we're on home page)

        Returns:
            bool: True if search visible
        """
        return self.is_displayed(self.SEARCH_CONTAINER)

    def click_search_box(self):
        """
        Click on search container to open search

        Returns:
            SearchPage: Returns SearchPage object (we navigate there)
        """
        self.click(self.SEARCH_CONTAINER)
        print("✓ Clicked search box")

        return SearchPage(self.driver)

    def search_for(self, search_term):
        """
        Complete search action: click search, type, and search

        Args:
            search_term: What to search for

        Returns:
            SearchPage: Search results page
        """
        # Click search box (opens search screen)
        search_page = self.click_search_box()

        # Type search term
        search_page.enter_search_text(search_term)

        return search_page