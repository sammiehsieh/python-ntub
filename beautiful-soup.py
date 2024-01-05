from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <button id="btn1" class="btn btn-success">我是按鈕1</button>
    <button id="btn2" class="btn btn-success">我是按鈕2</button>

    <input type="text">
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
    </ul>
    <div>
        <div>I am div1</div>
        <div id="div1" class="btn">I am div2</div>
    </div>
</body>

</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup)
# print(soup.button) # 比較建議寫成 soup.find('button')，比較能夠知道是找<button>而不是python的變數
# print(soup.button.string) # 找內文
# print(soup.button.get('id'))
# print(soup.find_all('button'))

# for btn in soup.find_all('button'):
#     print(btn.string)

print(soup.find(id='btn1'))
print(soup.find_all('div', id='div1')) # list
print(soup.find(class_='btn'))