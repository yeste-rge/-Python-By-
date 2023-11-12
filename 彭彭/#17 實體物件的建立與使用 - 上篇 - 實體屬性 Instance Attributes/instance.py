# Point 实体物件大的设计:平面坐标上的点
# class Point:
#     # 定义一个实体物件的初始化函数
    
#     # x,y 表示当前实体物件的坐标

# ##  def__init__(self):
#     def __init__(self,x,y): # self 表示当前实体物件本身，可以理解为当前实体物件的一个引用
#     ##  self.x=3    
#         self.x=x #表示当前实体物件的坐标
#     ##  self.y=4  
#         self.y=y #表示当前实体物件的坐标      
# # 建立第一个实体物件
# #p1=Point()
# p1=Point(3,4)
# print(p1.x,p1.y)
# # 建立第二个实体物件
# #p2=Point()
# p2=Point(5,6)
# print(p2.x,p2.y)

#FullName 实体物件的设计: 分开计入姓(First Name)、名(Last Name)资料的全名
class FullName:
    # def __init__(self):
    def __init__(self,first,last):
       #self.first="Peng" 
        self.first=first
    #   self.last="C.W."
        self.last=last
#name=FullName()
name1=FullName("C.W.","Peng")
print(name1.first,name1.last)
name2=FullName("T.Y.","Lin")
print(name2.first,name2.last)
name3=FullName("S.W.","Liu")
print(name3.first,name3.last)