import pandas as pd

# pchome
import pchome

data_pchome = []
for g in pchome.res_prods:
    data_pchome.append({
        '品名': g['Name'],
        '售價': g['Price']
    })

df_pchome = pd.DataFrame(data_pchome)
print(df_pchome)


# momo
# import momo

# data_momo = []
# for g in momo.res_prods:
#     data_momo.append({
#         'Name': g['goodsName'],
#         'Price': g['goodsPrice']
#     })

# df_momo = pd.DataFrame(data_momo)
# print(df_momo)


# 食べログ
# import requests
# from bs4 import BeautifulSoup

# url = "https://tabelog.com/osaka/rstLst/yakiniku/?vs=1&sa=%E5%A4%A7%E9%98%AA%E5%BA%9C&sk=%25E7%2584%25BC%25E8%2582%2589&lid=hd_search1&svd=20210707&svt=1900&svps=2&hfc=1&RdoCosTp=2&cat_sk=%E7%84%BC%E8%82%89"

# res = requests.get(url)
# soup = BeautifulSoup(res.text, 'html.parser')
# target = soup.find('div', class_='list-rst__rst-data')

# data = []
# for target in soup.find_all('div', class_='list-rst__rst-data'):
#   try:
#     shop_name = target.find('a').string
#     shop_star = target.find('span').string
#     # print(shop_name, shop_star)
#     data.append({
#         'name': shop_name,
#         'star': float(shop_star)
#     })
#   except:
#     pass

# df = pd.DataFrame(data)
# print(df)