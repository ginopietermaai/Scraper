from bs4 import BeautifulSoup
import requests
 

# get content of website and parse it
website_request = requests.get('https://arval.nl/public/herinzetlijst/', timeout=5)
website_content = BeautifulSoup(website_request.content, "html.parser")
    
# extract job description
container = website_content.find_all(class_ = 'grid-container')[-1]
table = container.find_all('table')
f = open('output.txt', 'w')
f.write(str(table).strip("[']"))
f.close()

# instantiate options 
#options = webdriver.ChromeOptions() 
 
# run browser in headless mode 
#options.headless = True 
 
# instantiate driver 
#driver = webdriver.Chrome(service=ChromeService( 
#	ChromeDriverManager().install()), options=options) 
 
# load website 
#url = 'https://arval.nl/public/herinzetlijst/' 

# get the entire website content 
#driver.get(url) 
#wait = WebDriverWait(driver, 40)
#wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "grid-container")))


# select elements by class name 
#element = driver.find_elements(By.CLASS_NAME, 'grid-container')[-1] 

#print(element.text)

#https://api.telegram.org/bot5980362577:AAGMqqy4nSZPrxdL6KLboDalAE6DQRJ3z2o/sendMessage?chat_id=5748584641&text=ginoooooo2