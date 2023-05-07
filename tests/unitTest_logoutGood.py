
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):

        driver = self.driver
        driver.maximize_window()
        user = "testuser"
        pwd = "test123"
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(3)
        elem = driver.find_element(By.ID,"id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID,"id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id=\"navbarSupportedContent\"]/ul[2]/li/a").click()

        time.sleep(5)
        try:
            elem = driver.find_element(By.XPATH,("//*[text()='Logged out!']"))
            self.driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("Logged out does not appear when Log out clicked")

        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
