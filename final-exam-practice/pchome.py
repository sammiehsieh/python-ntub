import requests

url = "https://ecshweb.pchome.com.tw/search/v4.3/all/results?q=%E9%9B%BB%E6%9A%96%E5%99%A8&page=1&sort=rnk/dc"

response = requests.get(url)
res_json = response.json()
res_prods = res_json['Prods']

for p in res_prods:
    # print(p['Name'], "\t", p['Price']) # \t = tab
    pass