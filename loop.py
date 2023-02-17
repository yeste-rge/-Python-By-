#Python 零基礎新手入門 #05 For Loop (迴圈)
#Loop (迴圈)
数列 = [1,2,3,4,5,6]
清单 = []
#for 数字 in 数列:
    #if 数字 > 3:
        #清单.append(数字)
#print(清单)[4, 5, 6]


# 乘积 = 1
#for 数字 in 数列:
    #乘积 *= 数字
#print(乘积)720
# *= ←可让清单中的数值彼此相乘 

数列 = [1,-2,3,-4,5,-6]
正值 = []
负值 = []
for 数字 in 数列:
    if 数字 > 0:
        正值.append(数字)
    else:
        负值.append(数字)
print(f"正值的数字包含了{正值}")
#正值的数字包含了[1, 3, 5]
print(f"正值的数字包含了{负值}")
#正值的数字包含了[-2, -4, -6]

#Range范围(起始值,结束值,间距值)
#for x in range(3):
    #print(x) 0 1 2
#for x in range(5):
    #print(x) 0 1 2 3 4 