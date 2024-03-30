# from django.test import TestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select

# class Hosttest(TestCase):
    
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(10)
#         self.live_server_url = 'http://127.0.0.1:8000/'

#     def tearDown(self):
#         self.driver.quit()

#     def test_02_login_page(self):
#         driver = self.driver
#         driver.get(self.live_server_url)
#         driver.maximize_window()
#         time.sleep(2)
#         theme=driver.find_element(By.CSS_SELECTOR,"a[href='/login']")
#         theme.click()
#         time.sleep(1)
#         elem = driver.find_element(By.NAME, "email")
#         elem.send_keys("vini@gmail.com")
#         elem = driver.find_element(By.NAME, "pwd")
#         elem.send_keys("Vini@1")
#         submit_button = driver.find_element(By.CSS_SELECTOR, "button#login_submit")
#         # Use WebDriverWait to wait for the button to become clickable
#         wait = WebDriverWait(driver, 10)
#         submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#login_submit")))
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class Hosttest(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/'

    def tearDown(self):
        self.driver.quit()

    def test_02_login_page(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        
        # Login process
        login_link = driver.find_element(By.CSS_SELECTOR, "a[href='/login/']")
        login_link.click()
        
        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys("anvy@gmail.com")
        
        password_input = driver.find_element(By.NAME, "pwd")
        password_input.send_keys("Anvy@1")
        
        login_button = driver.find_element(By.CSS_SELECTOR, "button#login_submit")
        login_button.click()
        
        # Navigating to the desired page
        service_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.nav-link.dropdown-toggle[data-bs-toggle='dropdown']"))
        )
        service_dropdown.click()
        
        shuttleclass_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.dropdown-item[href='/private_shuttleclass/']"))
        )
        shuttleclass_option.click()
        
        # Navigating to the registration form
        beginner_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-primary[href='/beginner/']"))
        )
        beginner_button.click()
        
        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-primary"))
        )
        register_button.click()
        
        # Filling the registration form
        name_input = driver.find_element(By.CSS_SELECTOR, "input#name.form-control.bg-light.border-0.px-4[name='name']")
        name_input.send_keys("Vini Vinod")
        
        email_input = driver.find_element(By.CSS_SELECTOR, "input[type='email'][name='email'].form-control.bg-light.border-0.px-4")
        email_input.send_keys("vini2@gmail.com")
        
        contact_input = driver.find_element(By.CSS_SELECTOR, "input[type='text'][id='contact-number'][name='contact-number'].form-control.bg-light.border-0.px-4")
        contact_input.send_keys("9865874748")
        
        # Selecting the game level
        game_level_select = Select(driver.find_element(By.CSS_SELECTOR, "select#game-level"))
        game_level_select.select_by_value("beginner")
        
        # Inputting the date
        input_date = "2000-12-20"  # Corrected date format
        date_input = driver.find_element(By.CSS_SELECTOR, "input#dob")
        date_input.send_keys(input_date)
        
        # Clicking the submit button
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
        )
        submit_button.click()

      
        # button_element = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary.w-100.py-3[type="submit"]')
        # button_element.click()
        # time.sleep(2) 
        # button_element = driver.find_element(By.CSS_SELECTOR, 'a[href="/"]')
        # button_element.click()
        # time.sleep(2)








        service = driver.find_element(By.CSS_SELECTOR, "a.nav-link.dropdown-toggle[data-bs-toggle='dropdown']")
        service.click()
        time.sleep(1) 
        element = driver.find_element(By.CSS_SELECTOR, 'a.dropdown-item[href="/shop/"]')
        element.click()
        
# Find the element using CSS selector
        element = driver.find_element(By.CSS_SELECTOR, 'span.add-to-cart')
        # element = driver.find_element(By.CSS_SELECTOR, 'i.fa.fa-shopping-cart')
        element = driver.find_element(By.CSS_SELECTOR, 'a.cart-button')
        element.click()
        element = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-success.btn-lg > span')
        element.click()
        element = driver.find_element(By.CSS_SELECTOR, 'a.links[href="/my-order/"]')
        element = driver.find_element(By.CSS_SELECTOR, 'a.links[href="/"]')
        # self.assertTrue(True, "Test Passed")

        if "http://127.0.0.1:8000/" in driver.current_url:
            print("Test Passed")
        else:
            print("Test Failed")
        self.assertIn("http://127.0.0.1:8000/", driver.current_url)
    if __name__ == 'main':
        import unittest
        unittest.main()
      
        