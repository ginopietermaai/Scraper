from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.support import expected_conditions as EC
 
# instantiate options 
options = webdriver.ChromeOptions() 
 
# run browser in headless mode 
options.headless = True 
 
# instantiate driver 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 
 
# load website 
url = 'https://arval.nl/public/herinzetlijst/' 

# get the entire website content 
driver.get(url) 
#wait = WebDriverWait(driver, 40)
#wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "grid-container")))


# select elements by class name 
element = driver.find_elements(By.CLASS_NAME, 'grid-container')[-1] 

print(element.text)