# def buy(item: str = 'black tea', sugarPercent: int = 30) -> str:
#     # print(f'I want to drink {item}')
#     """
#     introduction of buy function
#     @param item: string
#     @return: string
#     """

#     return f'iced {item} with {sugarPercent}% sugar'

# # drink1 = buy('americano', 0)
# # drink2 = buy('latte')
# # print(drink1, drink2)

# drink3 = buy()
# drink4 = buy(sugarPercent=50)
# print(drink3, drink4)

import requests
url = "https://ecshweb.pchome.com.tw/search/v4.3/all/results?q=%E8%A1%9B%E7%94%9F%E7%B4%99&page=1&sort=rnk/dc"
res = requests.get(url) # 使用 get 方法
# print(res.status_code) # 印出回覆的狀態碼
# print(res.text) # 讀取並印出 text 屬性
resjson = res.json()

prods_Name = resjson["Prods"][0]["Name"]
print(prods_Name)

prods_Price = resjson["Prods"][0]["Price"]
print(prods_Price)