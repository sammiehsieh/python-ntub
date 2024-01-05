import requests
import json

url = "https://ecshweb.pchome.com.tw/search/v4.3/all/results?q=衛生紙&page=1&sort=rnk/dc"

# res = requests.get(url)

# print(res)
# print(res.text)
# print(res.status_code)

# res_dict = json.loads(res.text)
# res_dict = res.json()

# print(res_dict["Prods"][0]["Name"])

for i in range(1, 11): # page 1, 2, 3 ... 10
    res = requests.get(url.format(i))
    res_dict = res.json()

    for prod in res_dict["Prods"]:
        print(prod['Name'], "\t", prod["Price"])

