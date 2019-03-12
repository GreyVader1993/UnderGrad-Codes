#first do pip install selenium in virtualenv

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BoothsTesting(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_default(self):
		self.driver.get("http://localhost:5000")
		self.assertIn("Booth's",self.driver.title)

		submitBtn = self.driver.find_element_by_id("submitBtn")
		submitBtn.click()

		self.assertIn("Success !", self.driver.page_source)


	def test_positive(self):
		self.driver.get("http://localhost:5000")
		self.assertIn("Booth's", self.driver.title)

		multiplier = self.driver.find_element_by_id("multiplier")
		multiplicand = self.driver.find_element_by_id("multiplicand")
		submitBtn = self.driver.find_element_by_id("submitBtn")

		multiplier.clear()
		multiplicand.clear()

		multiplier.send_keys("14")
		multiplicand.send_keys("-4")

		submitBtn.click()

		self.assertIn("Success !", self.driver.page_source)


	def test_openapp(self):
		self.driver.get("http://localhost:5000")
		self.assertIn("Booth's", self.driver.title)

		multiplier = self.driver.find_element_by_id("multiplier")
		multiplicand = self.driver.find_element_by_id("multiplicand")
		submitBtn = self.driver.find_element_by_id("submitBtn")

		multiplier.clear()
		multiplicand.clear()

		multiplier.send_keys("asda")
		multiplicand.send_keys("asda")

		submitBtn.click()

		self.assertIn("Error !", self.driver.page_source)


	def tearDown(self):
		self.driver.close()


if __name__ == "__main__":
	unittest.main()
