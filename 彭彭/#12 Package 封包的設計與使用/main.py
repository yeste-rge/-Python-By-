#主程式
import geometry.point #geometry.point是模组的元整名称要包含它所属的封包(在代码中使用point模块中定义的函数、类或者变量等)
result=geometry.point.distance(3,4)
print("距离",result)
import geometry.line as line
result=line.slope(1,1,3,3) #(载入线段模组)
print("斜率",result)