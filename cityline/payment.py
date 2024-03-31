from sys import path
from os.path import dirname
path.append(dirname(dirname(__file__)))

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

from html_helper import find_element, find_elements, scroll_to_element
from setting import PAYMENT_SETTING

class PaymentPage:
  def __init__ (self, driver : WebDriver):
    self.driver = driver
    
  def run (self):
    if 'venue.cityline.com' in self.driver.current_url and 'shoppingBasket' in self.driver.current_url:
      self.__personal_information()
      self.__delivery_method()
      self.__payment_method()
      
      find_elements(By.CLASS_NAME, 'check-btn', self.driver)[0].click()
      
      sleep(1.0)
  
  def __fill_input (self, element : WebElement, value : str):
    scroll_to_element(self.driver, element)
    element.clear()
    element.send_keys(value)
    
  def __select_option (self, element : WebElement, value : str):
    scroll_to_element(self.driver, element)
    element = Select(element)
    for idx, option in enumerate(element.options):
      if value in option.text:
        element.select_by_index(idx)
  
  def __personal_information (self):
    pi = PAYMENT_SETTING['personal_information']
    self.__fill_input(find_element(By.ID, 'fullname', self.driver), pi['name'])
    self.__fill_input(find_element(By.ID, 'phone', self.driver), pi['phone'])
    self.__fill_input(find_element(By.ID, 'email', self.driver), pi['email'])
    self.__fill_input(find_element(By.ID, 'confirmEmail', self.driver), pi['email'])
    
  def __delivery_method (self):
    method = PAYMENT_SETTING['delivery_method']['delivery_method']    
    # select method
    find_element(By.CLASS_NAME, 'select-header', self.driver).click()
    sleep(0.2)
    find_elements(By.CLASS_NAME, 'select-item', self.driver)[method].click()
    sleep(0.2)
    
    if method == 0:
      self.__sf()
    else:
      self.__mail()
  
  def __sf (self):
    setting = PAYMENT_SETTING['delivery_method']['sf']
    self.__fill_input(find_element(By.ID, 'confirmPhone', self.driver), setting['phone'])
    
    fillings = [
      ('region', 'region'),
      ('city', 'city'),
      ('subArea', 'sub_area'),
      ('addr1', 'addr')
    ]
    for (element_id, key) in fillings:
      self.__select_option(
        find_element(By.ID, element_id, self.driver),
        setting[key]
      )
    
  def __mail (self):
    fillings = [
      ('city', 'city'),
      ('addr3', 'addr1'),
      ('postalCode', 'postal_code'),
      ('addr2', 'addr2'),
      ('addr1', 'addr3')
    ]
    for (element_id, key) in fillings:
      self.__fill_input(
        find_element(By.ID, element_id, self.driver),
        PAYMENT_SETTING['delivery_method']['mail'][key]
      )
      
  def __payment_method (self):
    setting = PAYMENT_SETTING['payment_method']
    method_idx = setting['method']
    
    btn = find_elements(By.CLASS_NAME, 'payment', self.driver)[method_idx]
    scroll_to_element(self.driver, btn)
    btn.click()
    
    if method_idx <= 3:
      self.__fill_input(find_element(By.ID, 'holder', self.driver), setting['info_1']['holder'])
      self.__fill_input(find_element(By.ID, 'card', self.driver), setting['info_1']['card'])
    
    if method_idx <= 2:
      self.__fill_input(find_element(By.ID, 'expiry', self.driver), setting['info_2']['expiry_month']+setting['info_2']['expiry_year'])
      self.__fill_input(find_element(By.ID, 'code', self.driver), setting['info_2']['code'])
