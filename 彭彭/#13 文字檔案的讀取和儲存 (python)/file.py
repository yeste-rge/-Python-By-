#储存档案
#file=open("data3.txt",mode="w",encoding="utf-8") #开启
# file.write("测试中文\n好棒棒") #操作
# file.close()#关闭
with open("data4.txt",mode="w",encoding="utf-8") as file:
    file.write("测试中文\n好棒棒")
 #with会自动 安全 可靠 把档案释放和关闭
#读取档案
#with open("data.txt" , mode="r" , encoding="utf-8") as file:
#    data=file.read()
#print(data)
#把档案中的数字资料，一行一行的读取出来，并计算总合
#sum=0
#with open("data.txt" , mode="r" , encoding="utf-8") as file:
    #for line in file:  #一行一行的读取
        #sum+=int(line) #把line的文字转换成数字
#print(sum)
 
#使用 JSON 格式读取、腹泻档案


