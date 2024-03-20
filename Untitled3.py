#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install requests')



# In[6]:


import requests

def fetch_data_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from API")
        return None

def sort_products_by_popularity(products):
    return sorted(products.values(), key=lambda x: int(x['popularity']), reverse=True)

def display_sorted_products(products):
    for product in products:
        print(f"Title: {product['title']}, Price: {product['price']}, Popularity: {product['popularity']}")

def main():
    url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
    data = fetch_data_from_api(url)
    if data:
        sorted_products = sort_products_by_popularity(data["products"])
        display_sorted_products(sorted_products)

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




