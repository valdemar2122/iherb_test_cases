from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest


class TestAmazon:

    search_list = ("magnesium", "calcium", "omega 3")
    
    def setup_method(self):
        service = Service("./chromedriver")
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(5)
        self.driver.get("https://ie.iherb.com/")

    @pytest.mark.parametrize("search_query", search_list)
    def test_iherb_search(self, search_query):

        search = self.driver.find_element(By.ID, "txtSearch")
        search.send_keys(search_query, Keys.ENTER)

        expected_text = f'\"{search_query}\"'
        actual_text = self.driver.find_element(By.XPATH, "//span[@class='orange']").text

        assert expected_text == actual_text, f"Error. Expected text {expected_text}, but actual text is {actual_text}"

    def teardown_method(self):
        self.driver.quit()
