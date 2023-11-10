#随机模组
import random
#随机选取
# data=random.choice([1,5,6,10,20])
# print(data)
# data=random.sample([1,5,6,10,20],3)
# print(data)

#随机调换排序(就是洗牌的概念)
# data=[1,5,8,20]
# random.shuffle(data)
# print(data)

#随机取得乱数
# data=random.random() # 0～1之间的随机乱数
# data=random.uniform(0.0,1.0) # 0.0～1.0之间的随机乱数
# data=random.uniform(60,100) # 60～100之间的随机乱数
# print(data)
#取得常态分配乱数

#平均数100，标准差10，得到的资料多数在 90～110 之间
# data=random.normalvariate(100,10)
# print(data)

# 平均数 0, 标准差5， 得到的资料【多数】在 -5～5 之间
# data=random.normalvariate(0,5)
# print(data)

#统计模组
import statistics as stat
# stat.mean([1,4,5,8])
# data=stat.mean([1,4,5,8])
# data=stat.median([1,2,3,4,5,8,100])
data=stat.stdev([1,2,3,4,5,8,100]) #stdev 资料的标准差/资料的散布状况
print(data)

# 平均数, 中位数， 标准差， 常态分配