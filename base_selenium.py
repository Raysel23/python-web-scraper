from log import msg_log
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BaseSeleniums:
    def __init__(self, retries=3):
        self.retries = retries
        self.html_pages = []
        self.logger = msg_log("selenium message->")

        # chrome options
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def safe_get(self, url):
        """safely open a url with retry logic"""
        for attempt in range(1, self.retries + 1):
            try:
                self.logger.info(f"selenium loading url:{url} -- attempt {attempt}")
                self.driver.get(url)
                return True
            except Exception as e:
                self.logger.error(f"failed to load {url} on attempt {attempt} -- {e}")
                time.sleep(2)
        self.logger.error(f"failed to load page after {self.retries} retries: {url}")
        return False

    def scroll_h(self, pause=2):
        """scrolling page until end of pages"""
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(pause)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if last_height == new_height:
                self.logger.info("reached end of page.")
                break
            last_height = new_height

    def next_pagination(self, next_selector, pause=2, max_pages=50):
        """handle pagination by clicking next button until no more pages"""
        page = 1
        while True:
            self.logger.info(f"scraping page {page}")
            self.scroll_h(pause)

            current_html = self.driver.page_source
            if current_html in self.html_pages:
                self.logger.info("Duplicate page detected, stopping pagination.")
                break
            else:
                self.logger.info(f"storing html of page {page}")
                self.html_pages.append(current_html)

            try:
                nxt_btn = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, next_selector))
                )
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", nxt_btn
                )
                nxt_btn.click()
                page += 1
                time.sleep(pause)

                if page > max_pages:
                    self.logger.info("Reached maximum page limit of 50. Stopping pagination.")
                    break

            except (NoSuchElementException, TimeoutException):
                self.logger.info("No more pages to scrape. Pagination ended.")
                break

    def close(self):
        self.driver.quit()