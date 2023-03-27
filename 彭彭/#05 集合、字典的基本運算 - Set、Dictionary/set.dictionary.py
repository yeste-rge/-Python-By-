# 集合的运算 

# in 和 not in 的运算
# s1={3,4,5}
# print(10 not in s1)

#两个集合的操作
s1={3,4,5}
s2={4,5,6,7}
# s3=s1&s2 # & 交集: 取得两个集合中,相同的资料 # {4, 5}
# s3=s1|s2 # | 联集: 取两个集合中的所有资料,但不重复取 # {3, 4, 5, 6, 7}
# s3=s1-s2 # - 差集: 从 s1 中,减去 s2 重叠的部分  # {3}
# s3=s1^s2 # ^ 反交集: 取两个集合中,不重叠的部分 # {3, 6, 7}
# print(s3)

# s=set("HEllo") # 把字串中的字母拆解成集合: set(字串)
# print("A" in s)

# 字典的运算: key-value 配对 

#(基本的操作)
# dic={"apple":"苹果","bug":"蟲蟲"}
# dic["apple"]="小苹果"
# print(dic["apple"]) #用dic变数名称取得字典
# print("tr" not in dic) #判断 key 是否存在 

#delete(删除)
# dic={"apple":"苹果","bug":"蟲蟲"}
# print(dic)
# del dic["apple"] #删除字典中的键值对 (key-value pair)
# print(dic)

#(偏复杂的语法)
dic={x:x*2 for x in [3,4,5]} # 从列表的资料产生字典
#中挂号[]是一个列表
#key 是 x , value 是 x*2
print(dic)