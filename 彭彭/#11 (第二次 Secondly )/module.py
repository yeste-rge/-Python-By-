# 载入内建 sys 模组并取得资讯
# import sys
# print(sys.platform)
# print(sys.maxsize)
# print(sys.version)

# 建立 geometry 模组,载入使用
# import geometry
# result=geometry.distance(1,1,5,5)
# print(result) # 5.656854249492381
# result = geometry.slope(1,2,5,6)
# print(result) # 1.0

# 调整搜寻模组的路径
import sys
sys.path.append("modules") #In the module's search path list [Add path新增路径]
print(sys.path) #Print the module search path搜寻路径
print("------------------")
import geometry
print(geometry.distance(1,1,5,5)) #5.656854249492381