from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Get user input
email = input("Enter your email: ")
password = input("Enter your password: ")
document_url = input("Enter the URL of the document: ")
text_to_type = input("Enter the text you want to type: ")
wpm = int(input("Enter the desired typing speed in words per minute: "))

# Create a headless browser instance
driver = webdriver.Chrome(options=webdriver.ChromeOptions().headless)

# Set implicit wait time
driver.implicitly_wait(10)  # Wait for up to 10 seconds for elements to appear

# Open the document in the headless browser
driver.get(document_url)

# Log in to the document
email_element = driver.find_element_by_id("email")
password_element = driver.find_element_by_id("password")
login_button = driver.find_element_by_id("login-button")

email_element.send_keys(email)
password_element.send_keys(password)
login_button.click()

# Explicitly wait for the document body element to be visible
wait = WebDriverWait(driver, 10)
document_body = wait.until(EC.visibility_of_element_located((By.ID, "document-body")))

# Type the text into the document
words = text_to_type.split()
num_words = len(words)
time_per_word = 60 / wpm

for word in words:
    document_body.send_keys(word)
    document_body.send_keys(Keys.SPACE)
    time.sleep(time_per_word)

# Save the document
save_button = wait.until(EC.element_to_be_clickable((By.ID, "save-button")))
save_button.click()

file_name_element = wait.until(EC.visibility_of_element_located((By.ID, "file-name")))
file_name_element.send_keys("MyDocument.docx")

save_button.click()

# Close the headless browser
driver.quit()
