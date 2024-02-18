# 参数的预设资料
# def power(base,exp=0): #base 是 kuasa tiga(三个平方) #exp 是 kuasa dua(两个平方)
#     print(base**exp) # 一个 * 是乘法 两个 **是开方(kuasa)
# power(3,2)
# power(4)

# 使用参数名称对应
# def divide(n1,n2):
#     print(n1/n2)
# divide(2,4)
# divide(n2=2,n1=4)

# 无限/不定 参数资料

# def is defines a function.
def avg(*ns): 
    #1.avg is the name of the function.
    #2.The asterisk星号 * to accept any number of arguments任意数量的参数 
    #(similar to variable arguments in other languages). 
    #3.ns is just a convention for naming this variable变量的命名约定.
    sum=0
    for n in ns: 
        #For loop iterates through each argument迭代每个参数 (n) passed传递 to the function.
        sum+=n 
        #In each iteration在每次迭代, the current argument's value (n) is added to the sum variable.
    print(sum/len(ns)) 
    # The average is calculated by dividing the total sum by the number of arguments (len(ns)).
# The calculated average(avg) is printed to the console.
#average平均数
avg(3,4) #Calculates the average of 3 and 4, which is 3.5.
avg(3,5,10) #Calculates the average of 3, 5, and 10, which is 6.
avg(1,4,-1,-8) #Calculates the average of 1, 4, -1, and -8, which is -1.