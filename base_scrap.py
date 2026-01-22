from log import msg_log
import time,requests

class BaseScraping():
    
    def __init__(self,retries=3):
        self.retries = retries
        self.failed_urls = []
        self.logger = msg_log("base-scrap")
        
    
    def send_req(self,url):
    
        for attempt in range(1,self.retries+1):
            try:
                self.logger.info(f"requesting url {url} attempt {attempt}")
                response = requests.get(url,timeout=10)
                # check if the request is not status code 200
                response.raise_for_status()
                return response
            except Exception as e:
                self.logger.warning(f"request failed to connect {url}--{e}")
                time.sleep(2)
        
        self.failed_urls.append(url)
        self.logger.info(f"failed all retries {url}")
        return None
            
                