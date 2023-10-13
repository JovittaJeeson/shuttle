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
        theme=driver.find_element(By.CSS_SELECTOR,"a[href='/login']")
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

        submit_button.click()
        time.sleep(2)
        browse = driver.find_element(By.CSS_SELECTOR, "a.nav-item.nav-link[href='/Event_On_Trend/']")
        browse.click()
        time.sleep(1)  # Add a delay to observe the page change

       
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
        # driver.execute_script("window.scrollBy(0, 300);")
#         # time.sleep(1)
#         chap = driver.find_element(By.CSS_SELECTOR, 'a[href*="/books/8/chapter/Text/part0007.xhtml/"]')
#         chap.click()
#         time.sleep(1)
#         driver.execute_script("window.scrollBy(0, 300);")
#         time.sleep(1)
#         driver.execute_script("window.scrollBy(0, -300);")
#         time.sleep(1)
#         options = driver.find_element(By.CSS_SELECTOR, 'button#options-button')
#         options.click()
#         options.click()
#         time.sleep(1)
#         select=driver.find_element(By.CSS_SELECTOR, 'select#font-style')
#         select.click()
#         time.sleep(1)
#         option1=driver.find_element(By.CSS_SELECTOR, 'select#font-style option[value="calibri"]')
#         option1.click()
#         time.sleep(1)
#         theme2=driver.find_element(By.CSS_SELECTOR, 'select#theme')
#         theme2.click()
#         time.sleep(1)
#         option2=driver.find_element(By.CSS_SELECTOR, 'select#theme option[value="light"]')
#         option2.click()
#         time.sleep(1)
#         theme2.click()
#         increaseFont=driver.find_element(By.CSS_SELECTOR, 'span.adjust-button#font-size-increase')
#         increaseFont.click()
#         increaseFont.click()
#         increaseFont.click()
#         increaseFont.click()
#         increaseFont.click()
#         time.sleep(1)
#         increasePad=driver.find_element(By.CSS_SELECTOR, 'span.adjust-button#content-padding-increase')
#         increasePad.click()
#         increasePad.click()
#         increasePad.click()
#         time.sleep(1)
#         increaseLine=driver.find_element(By.CSS_SELECTOR, 'span.adjust-button#line-spacing-increase')
#         increaseLine.click()
#         increaseLine.click()
#         increaseLine.click()
#         time.sleep(1)
#         options.click()
#         title=driver.find_element(By.CSS_SELECTOR,"div.book-title a")
#         title.click()
#         time.sleep(1)
#         driver.execute_script("window.scrollBy(0, 2000);")
#         time.sleep(2)
#         like = driver.find_element(By.CSS_SELECTOR,"div.like-button button.btn.btn-primary:first-child")
#         like.click()
#         time.sleep(2)
#         driver.execute_script("window.scrollBy(0, -2000);")
#         time.sleep(1)
#         toLibrary = driver.find_element(By.CSS_SELECTOR,"div.breadcrumb a:nth-child(2)")
#         toLibrary.click()
#         time.sleep(1)
#         search=driver.find_element(By.CSS_SELECTOR,"input#search-bar.search-bar")
#         search.send_keys('monk')
#         time.sleep(2)
#         search.send_keys('')
#         time.sleep(1)
#         navbar_user = driver.find_element(By.CSS_SELECTOR,".navbar-user")
#         action = ActionChains(driver)
#         action.move_to_element(navbar_user).perform()
#         profile = driver.find_element(By.CSS_SELECTOR, "div#dropdown-menu a[href='/user/profile']")
#         profile.click()
#         wait = WebDriverWait(driver, 10)
#         time.sleep(1)
#         bio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.list-group a:nth-child(2)")))
#         # bio=driver.find_element(By.CSS_SELECTOR, "div.list-group a:nth-child(2)")
#         bio.click()
#         time.sleep(1)
#         contact=driver.find_element(By.CSS_SELECTOR, "div.list-group a:nth-child(3)")
#         contact.click()
#         time.sleep(1)
#         time.sleep(1)
#         wait = WebDriverWait(driver, 10)
#         navbar_user = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.navbar-user.dropdown img.profile-image")))
#         action = ActionChains(driver)
#         action.move_to_element(navbar_user).perform()
#         logout = driver.find_element(By.CSS_SELECTOR, "div#dropdown-menu a[href='/accounts/logout']")
#         logout.click()
#         time.sleep(1)

#     # Add more test methods as needed

# if __name__ == '_main_':
#     import unittest
#     unittest.main()