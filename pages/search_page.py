
"""
Search Page - Wikipedia search screen
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class SearchPage(BasePage):
    """Wikipedia search page object"""

    SEARCH_INPUT = (AppiumBy.ID, 'org.wikipedia:id/search_src_text')
    SEARCH_RESULTS_LIST = (AppiumBy.ID, 'org.wikipedia:id/search_results_list')
    RESULT_TITLE = (AppiumBy.ID, 'org.wikipedia:id/page_list_item_title')

    
    def is_search_input_displayed(self):
        """
        Check if search input field is visible
        
        Returns:
            bool: True if search input visible
        """
        return self.is_displayed(self.SEARCH_INPUT)
    
    def enter_search_text(self, text):
        """
        Type text into search field
        
        Args:
            text: Search term to type
        
        Returns:
            SearchPage: Self for chaining
        """
        self.send_keys(self.SEARCH_INPUT, text)
        print(f"✓ Entered search text: {text}")
        return self
    
    def is_results_displayed(self):
        """
        Check if search results are showing
        
        Returns:
            bool: True if results visible
        """
        return self.is_displayed(self.SEARCH_RESULTS_LIST)
    
    def get_first_result_text(self):
        """
        Get text of first search result
        
        Returns:
            str: First result text
        """
        return self.get_text(self.RESULT_TITLE)
    
    def click_first_result(self):
        """
        Click on first search result
        
        Returns:
            ArticlePage: Article page object
        """
        self.click(self.RESULT_TITLE)
        print("✓ Clicked first result")