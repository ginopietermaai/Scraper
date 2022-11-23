from bs4 import BeautifulSoup
import requests

def crawling(website_link, link_class):    
    # get content of website and parse it
    website_request = requests.get(website_link, timeout=5)
    website_content = BeautifulSoup(website_request.content, 'html.parser')
    
    # extract data
    container = website_content.find_all(class_ = link_class)[-1]
    table = container.find_all('table')
    return str(table).strip("[']")