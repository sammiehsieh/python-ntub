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
    "searchValue": "熱水壺",
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
      "keyword": "熱水壺",
      "curPage": "1",
      "historyDoPush": False,
      "timestamp": 1704636319741
    },
    "flag": 2018,
    "serviceCode": "MT01",
    "addressSearchData": {},
    "adSource": "tenmax"
  }
})
headers = {
  'Content-Type': 'application/json',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

res_json = response.json()
res_prods = res_json['rtnSearchData']['goodsInfoList']

for g in res_prods:
    # print(g['goodsName'], '\t', g['goodsPrice'])
    pass