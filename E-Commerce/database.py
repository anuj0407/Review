import json
import os
file_path = "products.json"

def load_product_data():
    if not os.path.exists(file_path):
        with open(file_path,'w') as f:
            json.dump({},f)
        return {}
    with open(file_path,'r') as f:
        return json.load(f)



def save_product_data(data:dict):
    with open(file_path,'w') as f:
        json.dump(data,f,indent=4)
