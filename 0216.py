

menu = {"蘋果":50,"草莓":80,"鳳梨":60}
#print(menu)
購物清單 = []
購買水果 = input("請輸入想購買的水果(蘋果、草莓、鳳梨擇一)")
購物清單.append(購買水果)
print(購物清單)

print("你想買的水果有：" + 購買水果 +"、總價格為"+ str(menu[購買水果]) +"元")

折扣價錢 = int(menu[購買水果]*0.9)
print("水果攤周年慶打九折，原價"+ str(menu[購買水果]) +"元，折扣後" + str(折扣價錢)+"元")



"""
menu = []
menu.append(input("請輸入購買物品:"))
print(menu)
print("購物清單數量:" + str(len(menu)))
"""

"""
#姓名、年齡、職業

名片 = {}
名片["姓名"] = input("請輸入姓名")
名片["年齡"] = input("請輸入年齡")
名片["職業"] = input("請輸入職業")

print(名片)
"""

"""
name = input("請輸入姓名:")
age1 = input("請輸入年齡:")
work = input("請輸入職業:")
age2 = int(age1) + 5

print(f"你好，我是{name}，我今年{age1}歲，職業是{work}")
#print("你好，我是" + name + "，我今年" + str(age1) + "歲，職業是" + work)
print("五年後，我是" + str(age2) + "歲")
"""


"""

成績單 = {"小明":70,"小華":60,"小王":80}

print(成績單) #1~4

print(成績單["小華"]) #5

成績單["小美"]=90 #6

print(成績單)
print(len(成績單))

#成績單.pop("小明")
#print(成績單)

"""

"""
購物清單 = ["礦泉水","蘋果","衛生紙"]

購物清單.pop(-1)
購物清單.append("雞肉")

print(購物清單)

print(購物清單[1])

"""

"""

a = {"麵":50,"飯":30}

a.pop("飯")

print(a)

"""