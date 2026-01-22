import logging

def msg_log(name):
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    
    # save file handler(msg)
    
    file_handler = logging.FileHandler("scrap.log",encoding="utf-8")    
    file_handler.setFormatter(formatter)
    
    # console log  to show in  the terminal
    
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    
    # check if has duplicate
    
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console)
        
    return logger    
    