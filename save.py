import csv
import os
import json

def save_json(data,filename):
    """json file saver"""
    os.makedirs("Results",exist_ok=True)
    file_output = os.path.join("Results",f"{filename}.json")
    
    with open(file_output,"w",encoding="utf-8") as file:
        json.dump(data,file,ensure_ascii=False,indent =4)
    return file_output

def csv_save(data,filename):
    """csv file saver"""
    if not data or not isinstance(data,list): # ensure data is not empty and is a list
        raise ValueError("Data must be a non-empty list of dictionaries.")
    os.makedirs("Results",exist_ok=True)  
    file_output = os.path.join("Results",f"{filename}.csv")
    
    with open(file_output,"w",newline="",encoding="utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=data[0].keys())# filenames = header
        writer.writeheader()
        writer.writerows(data)
    return file_output