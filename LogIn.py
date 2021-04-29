from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# to test if user can log in with valid email and password, user is transferred to the account page
def testLogIn():
    base_url = "https://www.codecademy.com/login"
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(base_url)
    driver.implicitly_wait(10)

    email_field = driver.find_element(By.XPATH, "//input[@id='user_login']")
    email_field.send_keys("user.tests.2021.ca@gmail.com")

    password_field = driver.find_element(By.XPATH, "//input[@id='login__user_password']")
    password_field.send_keys("Test.pass123")

    email_field = driver.find_element(By.XPATH, "//button[@id='user_submit']")
    email_field.click()

    current_url = driver.current_url

    if current_url == "https://www.codecademy.com/learn":
        print("User is logged.Current url is " + current_url)

    else:
        print("User is not logged in")

    time.sleep(3)


test()
