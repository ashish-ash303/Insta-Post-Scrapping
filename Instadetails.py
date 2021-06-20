# Imports
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


options = webdriver.ChromeOptions()
# options.headless = True
driver = webdriver.Chrome(
    ChromeDriverManager().install(), options=options)


# Instagram Opening
driver.get(
    "https://www.instagram.com/accounts/login/?next=%2F&source=logged_out_half_sheet")
print("1")
time.sleep(2)


# Username input
username = driver.find_element_by_xpath(
    '//*[@id="loginForm"]/div/div[1]/div/label/input')
print("2")
# username = driver.find_element_by_name("username")
username.send_keys('username')
time.sleep(2)

# Password Input
password = driver.find_element_by_xpath(
    '//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys('Password')
print("4")
time.sleep(2)

# Login Button
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
print("5")
login.click()
print("6")
time.sleep(2)

# Not Now Buttons
not_now = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(),'Not Now')]"))).click()
not_now2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(),'Not Now')]"))).click()
print("7")

# SearchBar
time.sleep(3)
searchbar = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbar.clear()
searchbar.send_keys("Searchname")
print("8")
time.sleep(2)
searchbar.send_keys(Keys.ENTER)
searchbar.send_keys(Keys.ENTER)
print("9")

# Scrolling Through Pages
time.sleep(3)
driver.execute_script(
    "window.scrollTo(0,document.body.scrollHeight)", )

print("10")

time.sleep(3)
# Getting the Images
images = driver.find_elements_by_tag_name("img")
images = [image.get_attribute('src') for image in images]
print("11")

# DataFrame
df = pd.DataFrame(images)
print(df)
df.to_csv('Uploads.csv')
