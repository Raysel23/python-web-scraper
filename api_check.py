import requests
from log import msg_log
logger = msg_log("api_check")

def api_request_check(url):
    
    """check if it api or not"""
    try:
        res = requests.get(url,timeout=10)
        res.raise_for_status()# Check for HTTP errors
        data = res.json()  # Try to parse JSON response
        # check if data is dict or list and not empty
        if isinstance(data,dict) or isinstance(data,list):
            if data:
                logger.info(f"API detected {url}")
                return True
            else:
                logger.info(f"Empty API response {url}")
                return False
        else:
            logger.info(f"Non-JSON response from {url}")
            return False
    except requests.exceptions.Timeout:
        logger.error(f"Request timeout for {url}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed for {url} --{e}")           
    return False        
        