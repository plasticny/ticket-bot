from selenium.webdriver import Chrome, ChromeOptions
from datetime import datetime
from time import sleep

from setting import BASE_SETTING
from cityline.tc import TcPage
from cityline.veune import VeunePage
from cityline.preformance import PreformancePage
from cityline.payment import PaymentPage

def wait_start ():
  start_time = datetime.strptime(BASE_SETTING['start_time'], '%Y-%m-%d %H:%M:%S')
  while datetime.now() < start_time:
    gap = start_time - datetime.now()
    print(f'[waiting] time left: {gap}')
    
    if gap.seconds > 0:
      sleep(1)
    else:
      sleep(gap.microseconds / 1000000)

if __name__ == "__main__":  
  options = ChromeOptions()
  options.add_argument(f'user-data-dir={BASE_SETTING["user_data_dir"]}')
  options.add_argument('--start-maximized')
  driver = Chrome(options=options)

  # wait_start()
  
  driver.get(BASE_SETTING['url'])
  
  TcPage(driver).run()
  VeunePage(driver).run()
  PreformancePage(driver).run()
  PaymentPage(driver).run()

  input('automation done, press enter to close the browser...')
