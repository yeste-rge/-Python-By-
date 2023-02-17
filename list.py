#List 清單(串列)
#存取清单资料⌈编号⌋
学生 = ["Ali","阿明","小杰","iqual"]
#print(学生[1:])['阿明', '小杰', 'iqual']从第1号同学一直数到最后一位喔
#print(学生[1:3])['阿明', '小杰']←⌈编号⌋也可以用⌈范围⌋的方式来表达,只是写1到3号的时候并不包含编号3号的同学
#print(学生[:3])['Ali', '阿明', '小杰']代表截取会从清单的最前面开始计算所以一共回传三个人
#print(len(学生))"4"
# print(学生[-2])"小杰" #（-negetive）负值时python会用逆向的方式查询 
#len(length长度(计算长度))的语法
#print(学生[1])"阿明"#print(学生[0])"Ali"
#print("/".join(学生))Ali/阿明/小杰/iqual #join结合

#直串与清单(串列)
唐诗 = "床前明月光"
#print(list(唐诗))"['床', '前', '明', '月', '光']" #list清单
#print(len(唐诗))"5"
#print(唐诗[2:])"明月光"
日期 = "2023/2/16"
#print(日期.split("/"))['2023', '2', '16']在挂号内标注分隔符号的类型就会被转成包含年，月，日的清单
#split(峰哥)语法

#修改清单资料(Change List Items)
学生 = ["Ali","阿明","小杰","iqual"]
#学生[1] = "小美" 
#print(学生) ['Ali', '小美', '小杰', 'iqual']
#list清单[] #tuple元组()
# tuple和list都可以拿来储存帮多笔的资料 许多指令也互相通用 唯一差别就在于tuple的资料不能修改和增减
#tuple元组()
#学生 = ("Ali","阿明","小杰","iqual")
#学生[1] = "小美" 
#print(学生)Traceback (most recent call last):
  #File "c:\Users\User\Documents\GitHub\-Python-By-\list.py", line 24, in <module>
    #学生[1] = "小美"
    #~~^^^
#TypeError: 'tuple' object does not support item assignment

#新增清单资料 Add List Items
#学生 = ["Ali","阿明","小杰","iqual"]
#学生.extend(["小美","小怡"])
#print(学生)['Ali', '阿明', '小杰', 'iqual', '小美', '小怡']
#学生.append("小美")
#print(学生)['Ali', '阿明', '小杰', 'iqual', '小美']

#删除清单资料Remove List Items
学生 = ["Ali","阿九","小杰","iqual"]
#学生.remove("阿九")
#print(学生)['Ali', '小杰', 'iqual']
#学生.pop()
#print(学生) ['Ali', '阿九', '小杰']
#pop的预设值是删除清单中最后一个项目 但也可以在挂号内输入清单编号
#学生.pop(1)
#print(学生)['Ali', '小杰', 'iqual']
#if "Ali" in 学生:
#    print("小明有在名单中")小明有在名单中
#print(学生.index("iqual"))3

#综合练习(学生成绩管理系统)
成绩系统 = ["小明",82,"小杰",94,"阿花",85]
操作 = input("请输入操作指令(A)查询(B)新增(C)删除(D)修改").upper()
if 操作 == "A":
    姓名 = input("请输入查询的姓名：")
    if 姓名 not in 成绩系统:
        print("查无此人")
    else:
        顺位 = 成绩系统.index(姓名)
        print(f"{姓名}的成绩是{成绩系统[顺位+1]}")
elif 操作 == "B":
    学生资料 = input("请输入要新增的姓名/成绩 (中间以斜线隔阂):")
    成绩系统.extend(学生资料.split("/"))
    print("成绩新增完毕")
    print(f"目前已登录的学生为{int(len(成绩系统)/2)}人")
elif 操作 == "C":
    姓名 = input("请输入删除的姓名：")
    姓名位置 = 成绩系统.index(姓名)
    成绩系统.pop(姓名位置)
    成绩系统.pop(姓名位置)
    print(成绩系统)
elif 操作 == "D":
    姓名 = input("请输入同学的姓名:")
    成绩 = input("请输入分数:")
    姓名位置 = 成绩系统.index(姓名)
    成绩系统[姓名位置+1] = 成绩
    print(成绩系统)