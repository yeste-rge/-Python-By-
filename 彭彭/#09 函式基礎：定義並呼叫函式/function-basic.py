# 定义函式

# 函式内部的程式码,若是没有做函式呼叫,就不会执行
# def multiply():
#     print(3*4)

# def multiply(n1,n2):
#     return n1*n2

# 呼叫函式

# value=multiply(3,4)+multiply(10,5) # (3+4)+(10+5)
# print(value)


# multiply(3,4)
# multiply(10,8)

# 程式的包装
def calculate(max):
    sum=0
    for x in range(1,max+1): 
        sum=sum+x
    print(sum)
calculate(10) # 1+2+3..+10
calculate(20)