import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
download_dir = os.path.abspath("download")  # Specify your download directory

# Create download directory if it doesn't exist
os.makedirs(download_dir, exist_ok=True)

# Configure Chrome options
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,  # Set download directory
    "plugins.plugins_disabled": ["Chrome PDF Viewer"],
    "download.prompt_for_download": True,       # Disable the download prompt
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True   # Automatically download PDFs
})
chrome_options.add_argument("--remote-allow-origins=*") # Add any other necessary arguments
driver = webdriver.Chrome(options=chrome_options)

# Function to download a file from a URL
def download_file(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)

# Visit the Labour Ministry website
driver.get("https://labour.gov.in/")

# Wait for the page to load and interact with the "Documents" menu
wait = WebDriverWait(driver, 20)  # Increased wait time

documents_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nav']/li[7]/a")))

actions = ActionChains(driver)
actions.move_to_element(documents_menu).perform()

monthly_progres_report = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nav']/li[7]/ul/li[2]/a")))
actions.move_to_element(monthly_progres_report).click().perform()
# monthly_progres_report.click

# time.sleep(5)
# documents_menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav"]/li[7]/a')))
# documents_menu.click()

# Wait for the dropdown menu to be visible and clickable
time.sleep(2)  # Short sleep to ensure the dropdown is visible

# Find and download the monthly progress reports
progress_reports_download_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='fontSize']//table[@role='Presentation']//tr[2]/td[2]/a")))
progress_reports_download_link.click()
time.sleep(2)
alert = wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()
# download_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='download']")))
pdf_url = progress_reports_download_link.get_attribute('href')
driver.get(pdf_url)
# driver.close()

time.sleep(10)
# progress_reports_link.click()

# Wait for the reports to be present and collect them
# reports = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, 'https://labour.gov.in/monthly-progress-report')]")))
# for report in reports:
#     report_url = report.get_attribute('href')
#     report_name = report_url.split("/")[-1]
#     download_file(report_url, os.path.join(os.getcwd(), report_name))
#     print(f"Downloaded {report_name}")

# # # Navigate back to the home page
# driver.get("https://labour.gov.in/")

# # Interact with the "Media" menu and go to the "Photo Gallery" submenu
# media_menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Media")))
# media_menu.click()
# photo_gallery_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Photo Gallery")))
# photo_gallery_link.click()

# # Create a folder to save photos
# photo_folder = os.path.join(os.getcwd(), "photo_gallery")
# os.makedirs(photo_folder, exist_ok=True)

# # Download the first 10 photos
# photos = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//img[@class='gallery-photo']")))
# photo_count = min(10, len(photos))
# for i in range(photo_count):
#     photo_url = photos[i].get_attribute('src')
#     photo_name = f"photo_{i + 1}.jpg"
#     download_file(photo_url, os.path.join(photo_folder, photo_name))
#     print(f"Downloaded {photo_name}")

# Close the browser
driver.quit()
