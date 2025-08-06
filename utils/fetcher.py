from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

class Browser:
    def __init__(self, wait_time=2):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--lang=fa-IR")
        options.add_argument("--window-size=1920x1080")
        self.driver = webdriver.Chrome(options=options)
        self.wait_time = wait_time

    def get_soup(self, url):
        try:
            self.driver.get(url)
            time.sleep(self.wait_time)
            html = self.driver.page_source
            return BeautifulSoup(html, "html.parser")
        except Exception as e:
            print(f"[❌] Error loading {url}: {e}")
            return None

    def close(self):
        self.driver.quit()
