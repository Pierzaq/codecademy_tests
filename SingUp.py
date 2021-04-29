from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# to test if user can sign up with invalid password, sign up button is not available
def testSignUp():
    base_url = "https://www.codecademy.com"
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(base_url)
    driver.implicitly_wait(10)

    email_field = driver.find_element(By.XPATH, "/html//input[@id='sign_up_form_email']")
    email_field.send_keys("test@gmail.com")

    password_field = driver.find_element(By.XPATH, "/html//input[@id='sign_up_form_password']")
    password_field.send_keys("123")

    sign_up_button = driver.find_element(By.XPATH, "//button[@id='sign_up_form_submit']")

    if not sign_up_button.is_enabled():
        print("User cannot sign up")

    password_field.clear()
    password_field.send_keys("Pass123")

    if sign_up_button.is_enabled():
        print("User can sign up")

    time.sleep(3)


test()
