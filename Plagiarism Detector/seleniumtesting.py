from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest

class Testing(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_openApp(self):
		self.driver.get("http://localhost:5000")
		self.assertIn("Plagiarism Detector", self.driver.title)

	def test_positive(self):
		self.driver.get("http://localhost:5000")
		inputText = self.driver.find_element_by_id("inputText")
		submitBtn = self.driver.find_element_by_id("submitBtn")

		inputText.clear()
		inputText.send_keys(
			"This problem is also arising with different entities like persons or companies. This article plays around with fuzzywuzzy, a Python library for Fuzzy String Matching. This is my plagiarism detector algorithm.")
		submitBtn.click()

		self.assertIn("Test Completed",self.driver.page_source)


	def test_negative(self):
		self.driver.get("http://localhost:5000")
		inputText = self.driver.find_element_by_id("inputText")
		submitBtn = self.driver.find_element_by_id("submitBtn")

		inputText.clear()
		submitBtn.click()

		self.assertIn("Error", self.driver.page_source)

	def tearDown(self):
		time.sleep(5)
		self.driver.close()

if __name__=="__main__":
	unittest.main()