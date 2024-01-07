import pandas as pd

grades = {
    "name": ["Mike", "Sherry", "Cindy", "John"],
    "math": [80, 75, 93, 86],
    "chinese": [63, 90, 85, 70]
}

df = pd.DataFrame(grades)
df.index = ['s1', 's2', 's3', 's4'] # 自訂索引值
df.columns = ["student_name", "math_score", "chinese_score"] # 自訂欄位名稱

print(df)