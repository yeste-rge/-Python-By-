# break 的简易名称
# n=0
# while n<5:
#     if n==3:
#         break
#     print(n) # 印出迴圈中的 n
#     n+=1
# print("最后的 n: ", n) # 印出迴圈结束后的 n

# continue 的简易范例
# n=0
# for x in [0,1,2,3]:
#     if x%2==0: # x 是偶数
#         continue
#     print(x)
#     n+=1
# print("最后的 n: ", n)

# else 的简易范例
# sum=0
# for n in range(11):
#     sum+=n
# else:
#     print(sum) # 印出 1+2+...+10 的结束

# 综合范例: 找出整数平方根
# 输入 9. 得到 3
# 输入 11，得到[没有]整数的平方根

# n=input("输入一个正整数: ")
# n=int(n) #转换输入成数字
# for i in range(n): # i 从 0 ～ n-1
#     if i*i==n:
#         print("整数平方根", i)
#         break # 用 break 强制结束迴圈时, 不会执行 else 区块
# else:
#     print("没有整数平方根") 

#myself
n=input("输入一个正整数(整数平方根/3次整数平方根/4次整数平方根): ")
n=int(n) #转换输入成数字
for i in range(n): # i 从 0 ～ n-1
    if i*i==n:
        print("整数平方根", i)
        break # 用 break 强制结束迴圈时, 不会执行 else 区块
    elif i*i*i==n:
        print("3次整数平方根", i)
        break
    elif i*i*i*i==n:
        print("4次整数平方根", i)
        break
else:
    print("没有整数平方根") 