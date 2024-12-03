from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.google.com")

# Validate the title
expected_title = "Bug Report Form"
actual_title = driver.title


driver.find_elements_by_tag_name('textarea')  #.send_keys('pepe')

# if expected_title == actual_title:
#     print("Title validation successful!")
# else:
#     print("Title validation failed. Expected:", expected_title, "Actual:", actual_title)

# Close the browser
input('')
driver.quit()