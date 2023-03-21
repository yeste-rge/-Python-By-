# 有序可变动列表 List 用中挂号[]
# grades=[12,60,15,70,90]
# grades[1:4]=[] # 连续删除列表中从编号 1 到编号 4(不包含) 的资料 
#把 60,15,70 删除并变成空白 整个列表就只剩 12 和 90

# grades=grades+[12,33] #在原本的列表中加 12 和 33
# length=len(grades) # 取得列表的长度 len(列表资料)
# print(length)
# grades[0]=55 #把 55 放到列表中的第一个位置
# print(grades[0])

# data=[[3,4,5],[6,7,8]]
# print(data)
# data[0][0:2]=[5,5,5]
# print(data)

# 有序不可变动列表 Tuple 用小挂号()
data=(3,4,5)
# data[0]=5 #错误: Tuple 的资料不可以变动
# print(data) #错误: Tuple 的资料不可以变动
print(data[0:2])