from sys import path
from os.path import dirname
path.append(dirname(dirname(__file__)))

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

from html_helper import find_element, find_elements, scroll_to_element
from setting import BASE_SETTING

class PreformancePage:
  def __init__ (self, driver : WebDriver):
    self.driver = driver

  def run (self):
    while 'venue.cityline.com' in self.driver.current_url and 'performance' in self.driver.current_url:
      self.__select_level()
      self.__select_number()
      
      purchase_btn_ls = find_elements(By.ID, 'expressPurchaseBtn', self.driver)
      for btn in purchase_btn_ls:
        if btn.is_displayed():
          btn.click()
          break
      break
    
    sleep(0.5)
    
  def __select_level (self):
    price_box = find_elements(By.CLASS_NAME, 'price', self.driver)[0]
    scroll_to_element(self.driver, price_box)
    
    price_item_ls = find_elements(By.CLASS_NAME, 'form-check', price_box)
    price_item_map = {}
    for item in price_item_ls:
      price_limited_block_ls = find_elements(By.CLASS_NAME, 'price-limited', item)
      
      if len(price_limited_block_ls) == 0 or 'status-title-soldout' not in price_limited_block_ls[0].get_attribute('innerHTML'):
        # if the level is not sold out
        level = find_elements(By.CLASS_NAME, 'price-degree', item)[0].text
        price_item_map[level] = item
        
    for level in BASE_SETTING['ticket_level']:
      if level in price_item_map:
        find_elements(By.CLASS_NAME, 'ticket-price-btn', price_item_map[level])[0].click()
        break
      
  def __select_number (self):
    Select(find_element(By.ID, 'ticketType0', self.driver))\
      .select_by_index(1)
      # .select_by_index(BASE_SETTING['ticket_num'])
