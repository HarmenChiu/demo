# data = ['紅茶', '10元'] # 清單中裝著一些整數
# # 請開始寫"寫入檔案"的程式碼

# with open('test.csv', 'w', encoding='utf-8') as f:
#     f.write('商品, 價格\n')
#     for d in data:
#         f.write(str(d) + ',')

import os

products = [] # 清單中裝著一些整數
if os.path.isfile('test01.csv'):
    print('檔案存在')
    
# 請開始寫"寫入檔案"的程式碼
    with open('test01.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().strip(',')
            products.append([name,price])
    print(products)
else:
    print('找不到檔案')