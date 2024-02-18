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
    sum=0 #Initializing初始 a variable sum to 0. This variable will store the running sum of the numbers.
    for x in range(1,max+1): 
        #Using a for loop to iterate through循环迭代 numbers from 1 to max (inclusive包含).
        #Inside the loop, adding the current number (x) to the sum variable.
        sum=sum+x
    print(sum) #After the loop, printing the final value of sum.
calculate(10) # 1+2+3..+10
# This calculates the sum of numbers from 1 to 10, which is 55.
calculate(20) #1+2+3..+20
# This calculates the sum of numbers from 1 to 20, which is 210.