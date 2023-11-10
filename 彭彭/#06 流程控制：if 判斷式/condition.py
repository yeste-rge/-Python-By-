#判断式
# x=input("请输入数字:") #取得字串形式的使用者输入
# x=int(x) #将字串形态转换成数字形态
# if x>200:
#     print("大于 200")
# elif x>100:
#     print("大于 100, 小于等于 200")
# else:
#     print("小于等于 100")

# 四则运算
n1=int(input("请输入数字1:"))
n2=int(input("请输入数字2:"))
op=input("请输入运算: + , - , * , / =")
if op=="+":
    print(f"{n1}加{n2}等于{n1+n2}") #后来改
#   print(n1+n2)    #原本
elif op=="-":
    print(f"{n1}减{n2}等于{n1-n2}") #后来改
#   print(n1-n2)    #原本
elif op=="*":
    print(f"{n1}除{n2}等于{n1*n2}") #后来改
#    print(n1*n2) #原本
elif op=="/":
    print(f"{n1}除{n2}等于{n1/n2}")  #后来改
#    print(n1/n2) #原本
else:
    print("不支援的运算 cao ni ma")