#Python 零基礎新手入門 #02 變數與資料型態
#input语法
姓名 = input("请输入你的姓名：")
出生年 = input("请输入你的出生年：")
年龄 = 2023 - int(出生年)

print(f"{姓名}你好，你出生于{出生年}，你今年是{年龄}岁。") 
#input语法回传的资料实际上都是str(字串)
# (x) 年龄 = "2023 - 2000" ('str'(string 字串)无法计算)
# (√)  年龄 = 2023 - 2000 (只有数字类型资料像int(整数)或float(小数)才可以)
# int(转成整数) float(转成浮点数) str(转成字窜)
# (x) "你今年是" + int + "岁"
# (√) "你今年是" + str + "岁"
#print(姓名 + "你好，你出生于" + 出生年 + "年，你今年是" + str(年龄) + "岁。")
# ←"注解"的意思