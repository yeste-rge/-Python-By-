#Python 零基礎新手入門 #07 Function (函式)
#def(Define(定义))
#格式：
#def的后面接着是函式的名称 #def 函式名称(引数)
#def hello_world(english版本)
def 打招呼(姓名,年纪):
    print(f"嗨,{姓名}今年是{年纪}岁")

#打招呼(年纪 = 20,姓名 = "小明")嗨,小明今年是20岁
#打招呼("小明",20)嗨,小明今年是20岁
#()←arguments(引数)给函式 函式在处理后可以回传一些有用的资讯给我们

折扣 = 0.9
def 总金额 (售价,运费 = 50):
#↑def 函式名称(引数 = 预设值)
    return int(售价 * 折扣 + 运费)
    print("此行会被忽略")
print(f"总金额为{总金额(售价 = 1000,运费 = 80)}元")
#print(f"总金额为{总金额(售价 = 1000, 运费 = 50)}元")
#return(回传)的语法才不会让计算结果直流在函式里面
#return通常会放在函式的最后一行
#def 总金额 (售价,运费):←def 函式名称(引数)