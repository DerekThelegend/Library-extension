
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
        # find 'All books' and click it – note this is all one Python statement
        driver.find_element(By.XPATH, "//*[@id=\"navbarSupportedContent\"]/ul[1]/li[2]/a").click()

        time.sleep(5)
        try:
            # verify Book List exists on new screen after clicking "All books" button
            # note that this test requires at least one book in the database to be successful
            elem = driver.find_element(By.LINK_TEXT, "Edit Book")
            self.driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("Book List does not appear when All books clicked")

        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
