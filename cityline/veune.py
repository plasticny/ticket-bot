from sys import path
from os.path import dirname
path.append(dirname(dirname(__file__)))

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep

from html_helper import find_element, find_elements

class VeunePage:
  def __init__(self, driver : WebDriver) -> None:
    self.driver = driver
  
  def run (self):
    ticket_card_clicked = False
    recaptcha_btn_clicked, recaptcha_done = False, False
    concurrent_login_done = False
    
    while 'venue.cityline.com' in self.driver.current_url and 'eventDetail' in self.driver.current_url:
      concurrent_login_model = find_element(By.ID, 'concurrentLoginModal', self.driver)
      recaptcha_block = find_element(By.ID, 'loginRecaptcha', self.driver)
      
      try:
        do_recaptcha_asked = recaptcha_block is not None and recaptcha_block.is_displayed()
        do_concurrent_login_asked = concurrent_login_model is not None and concurrent_login_model.is_displayed()
      except:
        do_recaptcha_asked = False
        do_concurrent_login_asked = False
      
      if do_recaptcha_asked and not recaptcha_done:
        print('recaptcha')
        recaptcha_done = self.__recaptcha(not recaptcha_btn_clicked)
        recaptcha_btn_clicked = True
      elif do_concurrent_login_asked and not concurrent_login_done:
        print('concurrent login')
        concurrent_login_done = self.__concurrent_login()
      elif not ticket_card_clicked:
        print('ticket card')
        ticket_card_clicked = self.__ticket_card()
        
    sleep(1.0)
    
  def __recaptcha (self, do_click_recaptcha : bool) -> bool:
    recaptcha_block = find_element(By.ID, 'loginRecaptcha', self.driver)
    login_model = find_element(By.ID, 'loginModal', self.driver)
    login_btn = find_elements(By.CLASS_NAME, 'btn-login', login_model)[0]
    
    sleep(1.5)
    
    if do_click_recaptcha:
      ActionChains(self.driver)\
        .move_to_element(recaptcha_block)\
        .move_by_offset(27, 37)\
        .click()\
        .perform()

    while not login_btn.is_enabled():
      pass
    login_btn.click()
    return True
  
  def __concurrent_login (self) -> bool:
    concurrent_login_modal = find_element(By.ID, 'concurrentLoginModal', self.driver)
    confirm_btn = find_elements(By.CLASS_NAME, 'confirm-btn', concurrent_login_modal)[0]
    confirm_btn.click()
    return True
  
  def __ticket_card (self) -> bool:
    self.driver.execute_script(f"window.scrollTo(0, window.scrollY+200)")
        
    ticket_card_ls = find_elements(By.CLASS_NAME, 'ticketCard', self.driver)
    if len(ticket_card_ls) == 0:
      print('no ticket card')
      return False
    
    btn_ls = find_elements(By.TAG_NAME, 'button', ticket_card_ls[0])
    if len(btn_ls) == 0:
      print('no button')
      return False

    btn_ls[0].click()
    return True