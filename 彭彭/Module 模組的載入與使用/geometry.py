#在 geometry 模组中定义几何运算功能
#计算俩个点的距离
def distance(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
#计算线段的斜率率
def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
