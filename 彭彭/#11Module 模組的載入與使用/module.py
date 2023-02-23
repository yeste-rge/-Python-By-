#这个不是papaya 電腦教室"我把视频放在下方
#Python Module 模組的載入與使用 By 彭彭 https://youtu.be/Et0DjY2cGiE
#载入内建的sys模组并使得资讯
#import sys as system
#print(system.platform)
#print(system.maxsize) 

#建立geometry模组，载入使用模组中定义的功能
#import geometry
#result=geometry.distance(1,1,5,5)
#print(result)
#result=geometry.slope(1,2,5,6)
#print(result) #1.0
#调整寻找模组的路径
import sys
sys.path.append("modules")#在模组的搜寻路径列表中【新增路径】
print(sys.path) #印出模组的搜寻路径列表
print("-----------------")
import geometry
print(geometry.distance(1,1,5,5))