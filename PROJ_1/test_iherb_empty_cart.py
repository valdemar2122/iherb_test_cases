from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestAmazon:

    def setup_method(self):
        service = Service("./chromedriver")
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(5)
        self.driver.get("https://ie.iherb.com/")

    def test_iherb_search(self):

        self.driver.find_element(By.ID, "truste-consent-button").click()

        self.driver.find_element(By.XPATH, "//a[@href='https://checkout1.iherb.com/cart']").click()

        expected_text = "Your shopping cart is empty"
        actual_text = self.driver.find_element(By.XPATH, "//div[@data-qa-element='empty-cart-description']").text

        assert expected_text == actual_text, f"Expected text is {expected_text}, but actual is {actual_text}"

    def teardown_method(self):
        self.driver.quit()
