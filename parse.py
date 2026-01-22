from bs4 import BeautifulSoup
from log import msg_log 

def parse_prod(html_p, logger):# logger parameter optional
    logger = logger or msg_log("parser message->")
    logger.info("start parsing products")
    
    products = []# stored products here

    for idx,html in enumerate(html_p,start =1):# enumerate html pages
        soup = BeautifulSoup(html,"html.parser")# parse html content
        # correct selectors for books scrap
        
        items = soup.select("article.product_pod")# select all product items
        logger.info(f"parsing page {idx}: {len(items)} products found")
        
        for item in items:
            title = item.select_one("h3 a")# get title element
            price = item.select_one("p.price_color")# get price element
            availability = item.select_one("p.instock.availability")# get availability element
            # append product details to list
            products.append({
                "title":title.get("title")if title else None,
                "price":price.get_text(strip=True)if price else None,
                "availability":availability.get_text(strip=True)if availability else None,
                "link":title.get("href")if title else None
            })
    
    logger.info(f"scraping completed:{len(products)} products found")
    return products        
    