#档案操作流程 
# 开启档案 > 读取或写入 > 关闭档案

#开启档案 
##基本语法
# 档案物件=open(档案路径,mode=开启模式) #开启是要写入还是读取或者读写都可以,这个叫"开启模式"
##开启模式
# 读取模式 - r
# 写入模式 - w
# 读写模式 - r+

#读取档案
##读取全部文字
# 档案物件.read()
#一次读取一行
#for 变数 in 档案物件:
#    从档案依序读取每行文字到变数中
#读取JSON格式
# import json #网络中交换资料存或者储存一些设定档我们都很喜欢用所谓的JSON的格式
# 读取到的资料=json.load(档案物件)

#写入档案
##写入文字
# 档案物件.write(字串)
#写入换行符号
# 档案物件.write("这是范例文字\n") #\n代表我们要换行用这个换行符号
#写入JSON格式
# import json
# json.dump(要写入的资料,档案物件)

#关闭档案
##基本语法 #这样才释放资源 这个是非常重要的动作 #在初期大家感觉不出来它的重要性 但是要建立习惯起来
# 档案物件.close()
##最佳实务
# with open(档案路径,mode=开启模式) as 档案物件:
#     读取或写入档案的程式
#你上去会会自动、安全的关闭档案