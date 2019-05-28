import re
str='malli 22 21-9-2019 rohit 33 22-12-2016 vinay 16 30-01-2000'
res=re.split(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(res)
