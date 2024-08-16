from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # or use webdriver.Firefox() for Firefox

try:
    # Navigate to the website
    driver.get("https://www.voipline.global/")
    
    # Wait for the page to load
    time.sleep(5)

    # Find and click the sign-up button or navigate to the sign-up page
    signup_button = driver.find_element(By.LINK_TEXT, "Sign Up")  # Adjust this selector as needed
    signup_button.click()

    # Wait for the sign-up page to load
    time.sleep(5)

    # Find the email input field and submit button
    email_field = driver.find_element(By.NAME, "email")  # Adjust this selector as needed
    submit_button = driver.find_element(By.NAME, "submit")  # Adjust this selector as needed

    # Enter email and submit the form
    email_address = "your-email@example.com"  # Replace with the desired email address
    email_field.send_keys(email_address)
    submit_button.click()

    # Wait for the page to update
    time.sleep(5)

    # Find the element that displays the email
    email_display_element = driver.find_element(By.XPATH, "//span[@id='email-display']")  # Adjust this XPath as needed

    # Print the email address
    print("Email displayed on page:", email_display_element.text)

finally:
    # Close the browser
    driver.quit()
