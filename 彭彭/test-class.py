# 定义类别、与类别的属性（封装在类别中的变数和函式)
# 定义一个类别 IO, 有两个属性 supportedSrcs 和 read
class IO: # input&output
    supportedSrcs=["console","file"] #类别的属性=["终端机","档案"]
    def read(src): #定义(define)函式叫做read, 参数叫 src # type: ignore
        if src not in IO.supportedSrcs: #利用类别属性操作取得支援的列表
            print("Not supported")
        else:
            print("Read from", src)
# 使用类别
print(IO.supportedSrcs) #类别的属性
#印出列表
IO.read("file")  # type: ignore #在一行代码后，表示这一行代码不进行类型检查。
#IO是类别的名称 ， read 是属性名称
#呼叫类别中的函式/属性
#类别的名称.属性的名称
#read 是个函式 可呼叫
IO.read("internet") # type: ignore