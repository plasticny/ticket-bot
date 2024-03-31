from sys import path
from os.path import dirname
path.append(dirname(dirname(__file__)))

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep

from html_helper import find_element

class TcPage:
  def __init__ (self, driver : WebDriver):
    self.driver = driver
  
  def run (self):
    while '.cityline.com/tc' in self.driver.current_url:
      btn = find_element(By.ID, 'buyTicketBtn', self.driver)
      if btn is None:
        continue
      
      btn.click()
      self.driver.switch_to.window(self.driver.window_handles[1])
    sleep(0.5)
