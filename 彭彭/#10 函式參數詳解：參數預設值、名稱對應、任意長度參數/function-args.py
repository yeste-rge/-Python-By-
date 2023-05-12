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
def avg(*ns):
    sum=0
    for n in ns:
        sum+=n
    print(sum/len(ns))
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)