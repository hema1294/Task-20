from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
driver = webdriver.Chrome()

# Open the CoWIN website
driver.get("https://www.cowin.gov.in/")

# Wait for the page to load and the elements to be clickable
wait = WebDriverWait(driver, 30)

# Find and click the "create FAQ" link
faq_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a')))
faq_link.click()

# Find and click the "partners" link
partners_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a')))
partners_link.click()

# Get the current window handle (home page)
main_window_handle = driver.current_window_handle

# Get all window handles
all_window_handles = driver.window_handles

# Display the window handles
for handle in all_window_handles:
    print(f"Window handle: {handle}")

# Switch to each new window and then close it
for handle in all_window_handles:
    if handle != main_window_handle:
        driver.switch_to.window(handle)
        print(f"Switched to window: {handle}")
        driver.close()

# Switch back to the main window
driver.switch_to.window(main_window_handle)
print(f"Switched back to main window: {main_window_handle}")

# Close the main browser window
driver.quit()
