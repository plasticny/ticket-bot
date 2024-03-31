# def queue_page (browser : WebDriver):
#   page_url = browser.current_url.split('?')[0]
  
#   while True:
#     try:
#       element = browser.find_element(By.ID, 'btn-retry-en-1')
#       while '7' not in element.text:
#         sleep(0.5)
#       element.click()

#       sleep(2)
      
#       if page_url != browser.current_url.split('?')[0]:
#         break
#     except:
#       pass