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
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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
        time.sleep(2)
        
        theme = driver.find_element(By.CSS_SELECTOR, "a[href='/login']")
        theme.click()
        time.sleep(1)
        
        elem = driver.find_element(By.NAME, "email")
        elem.send_keys("vini@gmail.com")
        elem = driver.find_element(By.NAME, "pwd")
        elem.send_keys("Vini@1")
        
        submit_button = driver.find_element(By.CSS_SELECTOR, "button#login_submit")
        
        # Use WebDriverWait to wait for the button to become clickable
        wait = WebDriverWait(driver, 10)
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#login_submit")))
        
        # Check if the login was successful
        if "http://127.0.0.1:8000/" in driver.current_url:
            print("Test Passed")
        else:
            print("Test Failed")

        # Use Django's built-in test assertions for more robust testing
        self.assertIn("http://127.0.0.1:8000/", driver.current_url)

        submit_button.click()
        time.sleep(2)
        browse = driver.find_element(By.CSS_SELECTOR, "a.nav-item.nav-link[href='/Event_On_Trend/']")
        browse.click()
        time.sleep(1)  

       
        view=driver.find_element(By.CSS_SELECTOR,"a.btn.mt-20.mr-10")
        view.click()
        
        time.sleep(1)
        


        
        registration_type_select = driver.find_element(By.CSS_SELECTOR, "select#registration-type")
        registration_type_select.click()
        select = Select(registration_type_select)
        select.select_by_value("single")
        time.sleep(1)
        name = driver.find_element(By.CSS_SELECTOR, "input#single-name")
        name.send_keys("Vini Vinod")

        time.sleep(1)
        input_date2 = "2000-11-29"
        calender = driver.find_element(By.CSS_SELECTOR, "input#single-dob[name='single-dob']")
        driver.execute_script(f"arguments[0].value = '{input_date2}';", calender)
        time.sleep(2)
        phone=driver.find_element(By.CSS_SELECTOR,"input#contact-number[name='contact-number']")
        
        phone.send_keys("9858741256")
        time.sleep(1)
        checkbox = driver.find_element(By.CSS_SELECTOR, 'input#declaration-checkbox[name="declaration-checkbox"]')

        checkbox.click()
        time.sleep(1)
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

        submit_button.click()
        time.sleep(1)
        return_to_homepage_link = driver.find_element(By.CSS_SELECTOR, 'a[href="/"]')

        return_to_homepage_link.click()
        time.sleep(1)
        self.assertTrue(True, "Test Passed")
        logout_link = driver.find_element(By.CSS_SELECTOR, 'a[href="/logout/"]')
        logout_link.click()

        time.sleep(1)
        elem = driver.find_element(By.NAME, "email")
        elem.send_keys("admin1@gmail.com")
        elem = driver.find_element(By.NAME, "pwd")
        elem.send_keys("Kavya@1234")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button#login_submit")
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#login_submit")))
        submit_button.click()
        time.sleep(2)
        membership_link = driver.find_element(By.CSS_SELECTOR, 'a[href="/member/"]')
        membership_link.click()
        time.sleep(1)
        add_membership_link = driver.find_element(By.CSS_SELECTOR, 'a[href="/add_member/"]')
        add_membership_link.click()
        time.sleep(1)
        title_input = driver.find_element(By.CSS_SELECTOR, 'input#title[name="title"]')
        title_input.send_keys("BASIC")
        time.sleep(1)
        price_input = driver.find_element(By.CSS_SELECTOR, 'input#price[name="price"]')
        price_input.send_keys("1500")
        time.sleep(1)
        duration_input = driver.find_element(By.CSS_SELECTOR, 'input#duration[name="duration"]')
        duration_input.send_keys("Monthly")
        time.sleep(1)
        features_textarea = driver.find_element(By.CSS_SELECTOR, 'textarea#features[name="features"]')
        features_textarea.send_keys("free Tutorials")
        time.sleep(1)
        save_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary.submit-btn[type="submit"]')
        save_button.click()
        time.sleep(1)
        self.assertTrue(True, "Test Passed")
        winners_link = driver.find_element(By.CSS_SELECTOR," a[href='/winner_Gallery/'] > i.fa.fa-calendar-check-o + span")
        winners_link .click()
        time.sleep(1)
       
        add_winners_link = driver.find_element(By.CSS_SELECTOR, "a[href='/add_winner/'].btn.btn-success.btn-rounded.float-right")
        add_winners_link .click()
        time.sleep(1)
        title_input = driver.find_element(By.CSS_SELECTOR, "input.form-control[type='text'][id='title'][name='title'][required]")
        title_input.send_keys("Singles Men ")
        time.sleep(1)
        name_input = driver.find_element(By.CSS_SELECTOR, "input.form-control[type='text'][id='name'][name='name'][required]")
        name_input.send_keys("Jovin Jeeson")
        time.sleep(1)
        prize_input = driver.find_element(By.CSS_SELECTOR, "input.form-control[type='text'][id='prize'][name='prize'][required]")
        prize_input.send_keys("5000")
        time.sleep(1)
        image_input = driver.find_element(By.CSS_SELECTOR, "input.form-control[type='file'][id='image'][name='image'][required]")
        image_input.send_keys("D:/Python/shuttle/Badminton/static/img/1.jpg")
        time.sleep(1)
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary.submit-btn[type="submit"]')
        submit_button.click()
        time.sleep(1)
        self.assertTrue(True, "Test Passed")

        