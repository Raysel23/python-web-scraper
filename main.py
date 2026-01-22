from base_selenium import BaseSeleniums
from base_scrap import BaseScraping
from save import save_json, csv_save
from parse import parse_prod
from api_check import api_request_check

URL = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

def run_scrap(url):  # main scraping function
    base = BaseScraping()
    if api_request_check(url):  # check if api is detected
        base.logger.info("API detected - using requests")

        res = base.send_req(url)  # send request
        if res:  # check if response is not None
            data = res.json()  # parse json data
            file_path = save_json(data, "api_products")  # save json file
            base.logger.info(f"Data saved to {file_path}")
    else:
        base.logger.info("No API detected - using selenium")
        selenium = BaseSeleniums()  # initialize selenium class
        all_products = []  # store all products

        if selenium.safe_get(url):  # safely get url
            selenium.scroll_h()  # use scrolling method to get all content
            selenium.next_pagination("li.next a")  # correct selector for next button

            # parse ALL collected pages
            for idx, html in enumerate(selenium.html_pages, start=1):
                selenium.logger.info(f"Parsing page {idx}")
                products = parse_prod(html, selenium.logger)
                all_products.extend(products)

            if all_products:  # check if products were found
                save_json(all_products, "selenium_products")
                csv_save(all_products, "selenium_products")
                base.logger.info(f"Total products scraped: {len(all_products)}")

        selenium.close()  # close selenium

if __name__ == "__main__":
    run_scrap(URL)