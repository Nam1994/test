from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    INPUT_USERNAME = (By.ID, 'user-name')
    INPUT_PASSWORD = (By.ID, 'password')
    BUTTON_LOGIN = (By.XPATH, "//*[@id='login-button']")

class ResultPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    LABEL_MESSAGE = (By.ID, 'flash')

class SauDemo(object):

    CHECK_OUT = (By.XPATH, "//*[@class='btn_action checkout_button']")
    INPUT_FIRSTNAME = (By.ID, 'first-name')
    INPUT_LASTNAME = (By.ID, 'last-name')
    INPUT_ZIPCODE = (By.ID, 'postal-code')
    CONTINUTE_BUTTON = (By.XPATH, "//*[@class='btn_primary cart_button']")
    FINISH_BUTTON = (By.XPATH, "//*[@class='btn_action cart_button']")
    CANCEL_BUTTON = (By.XPATH, "//*[@id='checkout_info_container']/div/form/div[2]/a")
    CONTINUTE_BUTTON_SHOPPING = (By.XPATH, "//*[@class='btn_secondary']")
    CLICK_BAG = (By.XPATH, "//*[@class='shopping_cart_container']")

    def ADD_TO_CART_BUTTON(index):
        x = "//div[@class='inventory_list']/div[@class='inventory_item']["
        z = "]//button"
       #print("abc" + str(index))
        #print(x + str(index) + z)
        return (By.XPATH, (x + str(index) + z))

    def REMOVE_TO_CART_BUTTON(index):
        x = "//div[@class='inventory_list']/div[@class='inventory_item']["
        z = "]//button"
       #print("abc" + str(index))
        #print(x + str(index) + z)
        return (By.XPATH, (x + str(index) + z))

    def REMOVE_TO_CART_IN_BAG(index):
        x = "//div[@class='cart_list']/div[@class='cart_item']["
        z = "]//button"
       #print("abc" + str(index))
        #print(x + str(index) + z)
        return (By.XPATH, (x + str(index) + z))
