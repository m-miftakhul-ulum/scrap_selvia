from bs4 import BeautifulSoup
import requests
import pandas as pd

url = requests.get("https://sellviacatalog.com/products?s=phone&page=3")
soup = BeautifulSoup(url.text, "html.parser")
list = soup.find(attrs={"class": "products_cont js-list_product"})

links = list.findAll("a")

gabung = []
for link in links:
    
    product_title = link.find('h4').text
    product_link = f"https://sellviacatalog.com{link['href']}" 
    
    product_url = requests.get(product_link)
    soup_url = BeautifulSoup(product_url.text, "html.parser")
    
    price = soup_url.find('input', {'name': 'salePrice'})
    desc = soup_url.find('div', {'class': 'wrap-content'})
    
    content_text = desc.get_text(strip=True)
   
   
   
    dict_item = {"judul": product_title, "product link": product_link, "price": price['value'], "description" : content_text }
    gabung.append(dict_item)


df = pd.DataFrame(gabung)
df.to_csv('datanya.csv', index=False)
df.to_excel('datanya.xlsx', index=False)

print("success")



