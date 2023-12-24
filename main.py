from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.neuralnine.com/")
driver.maximize_window()

links = driver.find_elements(By.XPATH, "//a[@href]")

for link in links:
    if "Books" in link.get_attribute("innerHTML"):
        link.click()
        break

# Use WebDriverWait to wait for the presence of book links
book_links_locator = (By.XPATH, "//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(.,'7 IN 1')]]][count(.//a)=2]//a")
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(book_links_locator))

book_links = driver.find_elements(*book_links_locator)
book_links[0].click()

driver.switch_to.window(driver.window_handles[1])

button_locator = (By.XPATH, "//a[.//span[text()[contains(.,'Paperback')]]]//span[text()[contains(.,'$')]]")
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(button_locator))

buttons = driver.find_elements(*button_locator)

for button in buttons:
    print(button.get_attribute("innerHTML"))
