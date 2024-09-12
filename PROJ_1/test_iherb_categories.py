from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestAmazonCategories:

    def setup_method(self):
        service = Service("./chromedriver")
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)
        self.driver.get("https://ie.iherb.com/")

    def test_iherb_search(self):

        self.driver.find_element(By.ID, "truste-consent-button").click()

        actual_text = self.driver.find_elements(By.XPATH, "//div[@class='link-bar']/div")

        assert len(actual_text) == 10, f"Expected len links is 10, but actual is {len(actual_text)}"

    def teardown_method(self):
        self.driver.quit()