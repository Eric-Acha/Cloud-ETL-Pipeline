import requests
import pandas as pd

def extract():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    df = pd.DataFrame(data)
    
    return df 