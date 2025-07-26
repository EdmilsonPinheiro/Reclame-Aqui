from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Navegador:
    def __init__(self):
        self.driver = None

    def create_driver_with_headers(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
        }

        chrome_options = Options()
        chrome_options.add_argument(f"user-agent={headers['User-Agent']}")
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        if self.driver:
            self.driver.quit()
