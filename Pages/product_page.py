from email import message

from Pages.base_page_object import BasePage
from Locators.locators import LoginPageLocators, SauDemo
from TestData.TestData import TestData
import logging

class ProductPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)

  def add_product_to_cart(self, index):
   # print("Productpage:" + str(index))
    self.click(SauDemo.ADD_TO_CART_BUTTON(index))

  def remove_product_to_cart_in_bag(self, index):
   # print("Productpage:" + str(index))
    self.click(SauDemo.REMOVE_TO_CART_IN_BAG(index))

  def click_bag_icon(self):
      logging.info("ADD a cart")
      self.click(SauDemo.CLICK_BAG)

  def click_checkout(self):
      logging.info("Checkoput")
      self.click(SauDemo.CHECK_OUT)

  def addcode(self, firstname, lastname, zipcode):
      self.enter_firstname(firstname)
      self.enter_lastname(lastname)
      self.enter_zipcode(zipcode)

  def enter_firstname(self, firstname):
      message = "Enter the username '{}'"
      logging.info(message.format(firstname))
      self.enter_text(SauDemo.INPUT_FIRSTNAME, firstname)

  def enter_lastname(self, lastname):
      message = "Enter the username '{}'"
      logging.info(message.format(lastname))
      self.enter_text(SauDemo.INPUT_LASTNAME, lastname)

  def enter_zipcode(self, zipcode):
      message = "Enter the username '{}'"
      logging.info(message.format(zipcode))
      self.enter_text(SauDemo.INPUT_ZIPCODE, zipcode)

  def click_continute(self):
      logging.info("click continute")
      self.click(SauDemo.CONTINUTE_BUTTON)

  def click_finish_button(self):
      logging.info("finish button")
      self.click(SauDemo.FINISH_BUTTON)

  def click_cancel_button(self):
      logging.info("finish button")
      self.click(SauDemo.CANCEL_BUTTON)

  def shopping_button(self):
      logging.info("shopping button")
      self.click(SauDemo.CONTINUTE_BUTTON_SHOPPING)

