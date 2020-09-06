from Pages.base_page_object import BasePage
from Locators.locators import CartLocators
from TestData.TestData import TestData
import logging

class CartPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    self.navigate_to(TestData.BASE_URL)

  def remove_product_to_cart_in_bag(self, index):
      # print("Productpage:" + str(index))
      self.click(CartLocators.REMOVE_TO_CART_BUTTON(index))

  def shopping_button(self):
        self.click(CartLocators.CONTINUTE_BUTTON_SHOPPING)

  def click_checkout(self):
        self.click(CartLocators.CHECK_OUT)



