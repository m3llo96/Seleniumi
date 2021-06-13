from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# Step 1) Open Firefox
browser = webdriver.Firefox(executable_path="C:\\Users\\user\\Downloads\\geckodriver\\geckodriver.exe")
# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
username.send_keys("testme@gmail.com")
WebDriverWait(browser, 3)
password = browser.find_element_by_id("pass")
password.send_keys("testme1999996")
#browser.find_element_by_css_selector("#u_0_d_ai").send_keys()

# Step 4) Click Login

wait = WebDriverWait(browser, 5 )
page_title = browser.title
assert page_title == "Facebook"


#by roeeddsadas
