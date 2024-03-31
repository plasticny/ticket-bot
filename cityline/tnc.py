from sys import path
from os.path import dirname
path.append(dirname(dirname(__file__)))

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from html_helper import find_element

class TncPage:
  """ the page after payment """
  def __init__ (self, driver : WebDriver):
    self.driver = driver
    
  def run (self):
    if 'venue.cityline.com' in self.driver.current_url and 'tnc' in self.driver.current_url:
      find_element(By.ID, 'check1', self.driver).click()
      find_element(By.ID, 'PRESENTER_PRIVACY', self.driver).click()
