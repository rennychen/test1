
"""
#布林值判斷
a = 10 > 5
b = 3 == 5
c = "Python" != "python"
d = len("apple") > 3
print(a)
print(b)
print(c)
print(d)
"""

"""
# 布林值判斷(進階)
price = int(input("請輸入消費金額:"))
if price > 100:
    print(price>100)
"""

"""
#if
age = int(input("請輸入年齡:"))

if age <= 18:
    print("未成年")
else:
    print("成年")
"""

"""
menu = ["a","b","c"]

order = input("請輸入餐點:")

if order in menu:
    print("ok")
else:
    print("輸入錯誤")
"""
"""
price = int(input("請輸入金額:"))

if price <= 500:
    print("未達折扣額度")
elif price >500 and price <= 1000:
    price = int(price*0.9)
    print("折扣後金額="+str(price))
else:
    price = int(price*0.8)
    print("折扣後金額="+str(price))

"""

"""
#if 分數評級
score = int(input("請輸入分數"))

if  score >= 90 and score <= 100: #也可以 90<=score<=100
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
elif score >= 0 and score <= 59:
    print("不及格")
else:
    print("輸入錯誤")

"""
"""
#輸入餐點名稱，並判斷它屬於哪一類

list1 = ["滷肉飯","雞肉飯","菜飯"]
list2 = ["炸雞腿","炸豬排","炸排骨"]
list3 = ["拉麵","烤土司"]

print(list1+list2+list3)
order = str(input("輸入餐點:"))
if order in list1:
    print("飯類餐點")
elif order in list2:
    print("炸物餐點")
elif order in list3:
    print("未知類別")
else:
    print("輸入錯誤")

#或是
#list = ["滷肉飯","雞肉飯","炸雞腿","炸豬排"]
#order = str(input("輸入餐點:"))
#if order == list[0] or list[1]
#   print("飯類餐點")
"""

"""
#巢狀if
age = int(input("請輸入年齡："))

if age<=13:
    if age<=6:
        print("免費入場")
    else:
        print("半價票")
elif 14<=age<=63:
    print("全票")
else:
    print("敬老票")
"""

"""
#if巢狀 分數評級
score = int(input("請輸入分數"))

if  score>100 or score<0:
    print("輸入錯誤")
else:
    if score >= 90 and score <= 100: #也可以 90<=score<=100
        print("A")
    elif score >= 80 and score <= 89:
        print("B")
    elif score >= 70 and score <= 79:
        print("C")
    elif score >= 60 and score <= 69:
        print("D")
    else:
        print("不及格")
"""

"""
#if 巢狀
price = int(input("請輸入金額："))
if price>=500:
    if price<=699:
        price = int(round(price*0.9,0))
        print("打九折，金額="+str(price))
    elif 700<=price<=999:
        price = int(round(price*0.85,0))
        print("打八五折，金額="+str(price))
    else:
        price = int(round(price*0.8,0))
        print("打八折，金額="+str(price)) 
else:
    print("未達優惠門檻")
"""

"""
#猜數字 (未完成)
ans = 63
x = int(input("請輸入0-100之中的一個數:"))
min =  0
max = 100

if 0<=x<=100:
    while ans != x:
        if x < ans:
            print(f"答錯，範圍為{x}~{max}")
            min = x
            x = int(input(f"請輸入{x}~{max}之中的一個數:"))
        elif x > :
            print(f"答錯，範圍為{min}~{x}")
            max = x
            x = int(input(f"請輸入{min}~{x}之中的一個數:"))
        else:
            print("答對")
elif ans == x:
    print("答對")
else:
    print("輸入錯誤") 
"""


"""

#for迴圈
num = 0

for i in range(1,10,2):
    print(i,end=" ")

"""

"""
list = ["貓","狗","兔"]

for i in range(0,3): #也可以寫 for i in list: ***執行有問題，待確
    print(list[i])

"""

"""
#for迴圈  建立價目表，並用for迴圈印出價目表所以項目及對應價錢
menu = {"飯":30,"麵":40,"湯":20}
list = ["飯","麵","湯"]

for i in range(0,3):
    print(list[i],menu[list[i]])

#或是
menu = {"飯":30,"麵":40,"湯":20}

for i in menu:
    print("項目:",i,"價錢",menu[i])
"""

"""
for i in range(1,11):
    print(i,end=" ")
    a = i%2
    if a==0:
        print("(此為偶數)",end=" ")
    
"""

"""
num = [5,12,8,3,15,7,20]
ans = 0

for i in range(0,7):  #或for i in num:
        if num[i]>=10:  #if i>10:
            ans +=  num[i]  #ans += i
            print(num[i],end=",")
print(f"大於10的總和={ans}")    
"""

"""
#while 設定計數器=0,讓計數器從1加到100

num = ans = 0

while num < 101:
    ans += num
    num +=1

print(ans)
"""

"""
#建立一個空購物清單，讓使用者點餐直到結束，並印出購物清單
list = []
add = 0

while add != "結束":
    add = input("請輸入購物項目(完成時請輸入\"結束\"):")
    list.append(add)

list.pop(-1)
print("購物清單內容為",list)

"""

"""
x = int(input("請輸入0-100之中的一個數:"))

while x<0 or x>100: #或 while not in range(1,101):
    x = int(input("輸入錯誤，請輸入0-100之中的一個數:"))

"""

"""
#輸入密碼
password = "python123"
user = input("請輸入密碼:")
error = 1

if password != user:
    while password != user:
        if error == 3:
            print("多次輸入錯誤，請稍後再試。")
            break
        elif password == user:
            print("登入成功")
            break
        else:
            user = input("密碼錯誤，請重新輸入密碼:")
            error += 1
if password == user:
    print("登入成功")

"""

"""
#輸入密碼參考答案

password = "123"
num = input("請輸入密碼")
次數 = 1

if num != password:
    while True:
        if 次數 < 3 :
            次數 += 1
            print("輸入錯誤，請重新再試")
            num = input("請輸入密碼")
        elif 次數 >= 3 :
            print("錯誤太多次，請稍後再試")
            break
        else :
            print("登入成功")
else :
    print("登入成功")
"""

"""
def add(a,b):
    ans = a+b
    print(ans)

add(30,9)
"""

"""
def add(x):
    print("字串長度="+str(len(x)))

add("今天2月23日")
"""
"""
def ans():
    print("5+3=8")

ans()
"""


def xx(x,y):
    print("%d的%d次方=%d" % (x,y,pow(x,y)))

xx(5,2)