#Python 零基礎新手入門 #05 For Loop (迴圈)
#Python 零基礎新手入門 #06 While Loop (迴圈)
#Loop (迴圈)
#数列 = [1,2,3,4,5,6]
#清单 = []
#for 数字 in 数列:
    #if 数字 > 3:
        #清单.append(数字)
#print(清单)[4, 5, 6]


# 乘积 = 1
#for 数字 in 数列:
    #乘积 *= 数字
#print(乘积)720
# *= ←可让清单中的数值彼此相乘 

#数列 = [1,-2,3,-4,5,-6]
#正值 = []
#负值 = []
#for 数字 in 数列:
    #if 数字 > 0:
        #正值.append(数字)
    #else:
        #负值.append(数字)
#print(f"正值的数字包含了{正值}")
#正值的数字包含了[1, 3, 5]
#print(f"正值的数字包含了{负值}")
#正值的数字包含了[-2, -4, -6]

#Range范围(起始值,结束值,间距值)
#for x in range(3):
    #print(x) 0 1 2
#for x in range(5):
    #print(x) 0 1 2 3 4 
#while True:
    #x  = input("请输入一个数字：")
    #if x == "不玩了":
        #print("再见!")
        #break
    #print(x)

#数字 = 1
#while 数字 <= 5:
  #print(数字)
  #数字 += 1
  #1 2 3 4 5
商品价格 = 1000
A玩家 = input("请输入第一位玩家的昵称: ")
B玩家 = input("请输入第二位玩家的昵称: ")
回答次数 = 1
总次数 = 3
while 回答次数 <= 总次数:
    A作答 = int(input(f"请{A玩家}输入商品金额: "))
    B作答 = int(input(f"请{B玩家}输入商品金额: "))
    if A作答 == 商品价格 or B作答 == 商品价格:
        break  
    elif abs(商品价格 - A作答) < abs(商品价格 - B作答):
#abs(absolute绝对值)的语法 并舍去负号，只截取金额中数字的部分
        print(f"{A玩家}的答案比较靠近价格")
    else:
        print(f"{B玩家}的答案比较靠近价格")
    回答次数 += 1    
if A作答 == 商品价格:
    print(f"{A玩家}猜对了!{A玩家}获胜!")
elif B作答 == 商品价格:
    print(f"{B玩家}猜对了!{B玩家}获胜!")
elif abs(商品价格 - A作答) < abs(商品价格 - B作答):
    print(f"游戏结束!正确的商品价格是{商品价格},{A玩家}的答案比较靠近,{A玩家}获胜!")
else:
    print(f"游戏结束!正确的商品价格是{商品价格},{B玩家}的答案比较靠近,{B玩家}获胜!")    