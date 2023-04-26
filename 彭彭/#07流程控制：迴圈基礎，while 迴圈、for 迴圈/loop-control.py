# break 的简易名称
n=0
# while n<5:
#     if n==3:
#         break
#     print(n) # 印出迴圈中的 n
#     n+=1
# print("最后的 n: ", n) # 印出迴圈结束后的 n

# continue 的简易范例
n=0
for x in [0,1,2,3]:
    if x%2==0: # x 是偶数
        continue
    print(x)
    n+=1
print("最后的 n: ", n)

# else 的简易范例
# 综合范例: 找出整数平方根