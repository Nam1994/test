from Pages.base_page_object import BasePage
from Locators.locators import CheckoutComplete
from TestData.TestData import TestData
import logging

class CartPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    pass
    self.navigate_to(TestData.BASE_URL)