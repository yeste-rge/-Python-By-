#List 清單(串列)
#存取清单资料⌈编号⌋
学生 = ["Ali","阿明","小杰","iqual"]
#print(学生[1:])['阿明', '小杰', 'iqual']从第1号同学一直数到最后一位喔
#print(学生[1:3])['阿明', '小杰']←⌈编号⌋也可以用⌈范围⌋的方式来表达,只是写1到3号的时候并不包含编号3号的同学
#print(学生[:3])['Ali', '阿明', '小杰']代表截取会从清单的最前面开始计算所以一共回传三个人
# print(len(学生))/print(学生[-2])"小杰"
#（-negetive）负值时python会用逆向的方式查询 
#len(length长度)的语法
#print(学生[1])"阿明"#print(学生[0])"Ali"