import requests
import json

url = "https://apisearch.momoshop.com.tw/momoSearchCloud/moec/textSearch"

payload = json.dumps({
  "host": "momoshop",
  "flag": "searchEngine",
  "data": {
    "specialGoodsType": "",
    "isBrandSeriesPage": False,
    "authorNo": "",
    "originalCateCode": "",
    "cateType": "",
    "searchValue": "聖誕節",
    "cateCode": "",
    "cateLevel": "-1",
    "cp": "N",
    "NAM": "N",
    "first": "N",
    "freeze": "N",
    "superstore": "N",
    "tvshop": "N",
    "china": "N",
    "tomorrow": "N",
    "stockYN": "N",
    "prefere": "N",
    "threeHours": "N",
    "video": "N",
    "cycle": "N",
    "cod": "N",
    "superstorePay": "N",
    "showType": "chessboardType",
    "curPage": "1",
    "priceS": "0",
    "priceE": "9999999",
    "searchType": "1",
    "reduceKeyword": "",
    "rtnCateDatainfo": {
      "cateCode": "",
      "cateLv": "-1",
      "keyword": "聖誕節",
      "curPage": "1",
      "historyDoPush": False,
      "timestamp": 1702896430875
    },
    "flag": 2018,
    "serviceCode": "MT01",
    "addressSearchData": {},
    "adSource": "tenmax"
  }
})
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)



res_json = response.json()

print(res_json['rtnSearchData']['goodsInfoList'][0]['goodsName'])

for good in res_json['rtnSearchData']['goodsInfoList']:
    print(good['goodsName'], good['goodsPrice'])