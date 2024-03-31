from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import Union

def find_element (by : By, value : str, container : Union[WebDriver, WebElement] = None) -> Union[WebElement, None]:
  try:
    return container.find_element(by, value)
  except:
    return None
  
def find_elements (by : By, value : str, container : Union[WebDriver, WebElement] = None) -> list[WebElement]:
  try:
    return container.find_elements(by, value)
  except:
    return []
  
def scroll_to_element (driver : WebDriver, element : WebElement):
  dest = element.get_attribute('offsetTop')
  driver.execute_script(f'window.scrollTo(0, {dest})')
