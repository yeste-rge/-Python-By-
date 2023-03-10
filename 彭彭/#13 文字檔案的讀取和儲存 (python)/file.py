#储存档案
#file=open("data3.txt",mode="w",encoding="utf-8") #开启 # 写入模式 - w
# file.write("测试中文\n好棒棒") #操作
# file.close()#关闭
# with open("data5.txt",mode="w",encoding="utf-8") as file: #with不需自己close 它会"自动","安全","可靠"把档案释放和关闭(ta会比计较好)
#    file.write("5\n3") 

#读取档案
#把档案中的数字资料，一行一行的读取出来，并计算总合
# sum=0
# with open("data5.txt", mode="r", encoding="utf-8") as file: # 读取模式 - r
#    for line in file: #一行一行的读取
#        sum+=int(line) #line转换成int(整数)加到总和
# print(sum) #把总和印出

#with open("data.txt" , mode="r" , encoding="utf-8") as file: # 读取模式 - r
    #for line in file:  #一行一行的读取
        #sum+=int(line) #把line的文字转换成数字
#print(sum)
 
#使用 JSON 格式读取、复写档案
import json
#从档案中读取 JSON 资料,放入 data 里面
with open("config.json", mode="r") as file: # 读取模式 - r
    data=json.load(file)
print(data) #data是一个字典资料
data["name"]="New Name" #修改变数中的资料
#把最新的资料复写回档案中
with open("config.json", mode="w") as file: 
    json.dump(data, file)