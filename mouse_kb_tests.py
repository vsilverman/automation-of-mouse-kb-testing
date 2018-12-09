"""
This program demonstrates data-driven automation of
mouse and keboard testing for the following sites:
    https://unixpapa.com/js/testmouse.html
    https://keyboardtester.co/keyboard-tester.html

Created on Nov 16, 2018

@version 1.0
@author: vlad
"""

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
# import os
import unittest
import time
# import re


class MyAutoActions(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.base_url = "https://unixpapa.com/js/testmouse.html"
        self.driver.get(self.base_url)

    def test_mouse_single_clicks(self):
        driver = self.driver
        # ERROR: Caught exception [unknown command [#]]
        for i in range(3):
            driver.find_element_by_link_text("click here to test").click()
            elem = driver.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='click here to test'])[1]/following::img[1]")
            elem.click()
            time.sleep(2)
            driver.find_element_by_link_text("click here to clear").click()

    def test_mouse_action_chains(self):
        driver = self.driver
        actionChains = ActionChains(driver)
        elem = driver.find_element_by_link_text("click here to test")
        actionChains.click(elem)
        actionChains.click(elem)
        actionChains.click(elem)
        time.sleep(2)
        actionChains.double_click(elem)
        actionChains.perform()
        time.sleep(2)

    def test_kb_single_clicks(self):
        driver = self.driver
        driver.get("https://keyboardtester.co/keyboard-tester.html")
        testarea = driver.find_element_by_id("testarea")
        testarea.click()
        for i in range(10):  # numbers from 0 to 9
            testarea.clear()
            testarea.send_keys(i)
            time.sleep(1)
        for char in "abcdefghijklmnopqrstuvwxyz":
            testarea.clear()
            testarea.send_keys(char)
            time.sleep(1)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
    
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    @classmethod
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
