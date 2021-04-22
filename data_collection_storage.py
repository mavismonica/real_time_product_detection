import csv
import json

def make_json(csvFilePath, jsonFilePath):
    r"""Converts a csv file into json.
    
    Parameters
    ----------
    csvFilePath : path
        path of the csv file.
    jsonFilePath : path
        path where the json file is to be saved along with the json name.

    Returns
    -------
    json converted csv file
    
    """
     
   
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary and add it to data
        for rows in csvReader:
                  
            key = rows['id']
            data[key] = rows
 
   
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
         

csvFilePath = r'C:/Users/mavis/thesis/real_time_product_detection/csvs/nutrition.csv'
jsonFilePath = r'C:/Users/mavis/thesis/real_time_product_detection/jsons/product_calorie.json'


make_json(csvFilePath, jsonFilePath)





