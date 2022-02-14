import os
import time
import random
from http.cookies import SimpleCookie

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from django.contrib.staticfiles.finders import find


TWEET_TEXT_SELECTOR = "article[role='article'] > div > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)"

def crawl_page(url,scroll_count=3):
    """
    request and crawl the page from the `url` parameter, and scroll down the page in order to load more data.
    the parameter `scroll_count` specifies how many times the page should be scrolled.
    """


    # Set chrome webdriver options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    # initialize chrome webdriver
    path = find("chromedriver_linux64/chromedriver")
    driver = webdriver.Chrome(options=chrome_options, executable_path=path)

    
    driver.get(url)
    tweets = []
    for i in range(1,scroll_count):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll down the page
        # time.sleep(random.randint(10,15)) # using random to avoid being blocked
        time.sleep(30)
        tweets.extend(driver.find_elements_by_css_selector(TWEET_TEXT_SELECTOR))
        
    
    return set(tweets)