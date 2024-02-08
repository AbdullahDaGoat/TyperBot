import pyautogui
import time
import webbrowser

# Get user input
email = input("Enter your email: ")
password = input("Enter your password: ")
document_url = input("Enter the URL of the document: ")
text_to_type = input("Enter the text you want to type: ")
wpm = int(input("Enter the desired typing speed in words per minute: "))

# Open the document in a browser
webbrowser.open(document_url)

# Log in to the document
pyautogui.click(x=100, y=100)  # Click on the login button
pyautogui.write(email)  # Type in the email address
pyautogui.press('tab')  # Press the tab key to move to the password field
pyautogui.write(password)  # Type in the password
pyautogui.press('enter')  # Press the enter key to log in

# Type the text into the document
words = text_to_type.split()
num_words = len(words)
time_per_word = 60 / wpm
total_time = time_per_word * num_words

for word in words:
    pyautogui.write(word)
    pyautogui.press('space')
    time.sleep(time_per_word)

# Save the document
pyautogui.click(x=200, y=200)  # Click on the save button
pyautogui.write("MyDocument.docx")  # Type in the file name
pyautogui.press('enter')  # Press the enter key to save the document
