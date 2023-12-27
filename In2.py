#Manipulating Strigs
# import math
# print(math.sqrt(81))
## print(math.pi)
#Handling multiple else statements with elif
# age=int(input("write your age:")) # must be use "int"
# if age < 21:
#     # if under 21, no alcohol
#     beverage = "milk"
# elif age >= 21 and age < 80:
#     # Ages 21-79, suggest beer / can drink alcohol
#     beverage = "beer"
# else:
#     # if 80 or older, prune juice might be a good choices.
#     beverage = "prune juice"

# print("Have a " + beverage)
#with for
# for x in range(7): # from 0 to 6 
#     print(x)
# print("Well done") # All done
# for w in range(1,11): #from 1 to 10
#     print(w)
# print("All done")
#for x in "snorkel": # s n o r k e l
#   print(x) /
# my_word = "snorkel" # s n o r k e l
# for w in my_word:
#   print(w)
# for x in["The", "Rain", "In", "Spain"]:
    # print(x) /
# seven_dwarves = ["Happy", "Grumpy", "Sleepy","Bashful","Sneezy","Doc","Dopey"]
# for r in seven_dwarves:
#     print(r)
# print("And Snow white too")
# answers=["A","C","","D"]
# for answer in answers:
#     if answer == "":
#         print("Incomplete")
#         break # Without any letters after, print will be one space 
#     print(answer)
# print("Loop is done")
# #Nesting loops
# #Outer loop
# for outer in ["first","second","third"]:
#     print(outer)
#     #Inner loo
#     for inner in range(3):
#         print(inner + 1)

# print("Both loops are done")
# #Out of both loops here
# counter = 65 
# while counter < 91: # 65=A -> 91=Z # 0=A (wrong) 
#     print(str(counter) + "=" + chr(counter))
#     counter += 1
# print("All done")

# import random
# print("Odd numbers") #奇数 e.g. 1,3,5 ...
# counter=0
# while counter < 10:
#     # Get a random number
#     number = random.randint(1,999) #Output: Could be any integer between 1 and 999(e.g. , 427,...)
#     if int(number /2)==number /2:
#         #If it's an even number, don't print it(若是偶数，则不打印)
#         continue
#     #Otherside, if it's odd, print it and increment the couter. (若是奇数，则打印并增加计数器)
#     print(number)
#     #Incorrect the loop counter.
#     counter+=1 # if counter=+1 the number will be not stopping 
#     #(creates a variable named counter and sets its initial value to 0.) 
#     #This counter will be used to track the number of odd numbers that have been printed.
#     #这行代码将 counter 的值增加 1，确保循环最终会在打印了 10 个奇数后终止。
#     #柜台
# print("Loop is done")
# #Keywords
# #The code effectively generates and prints 10 random odd numbers between 1 and 999.
# #此代码有效地生成并打印了 10 个 1 到 999 之间的随机奇数。
# # It uses a while loop to control the number of iterations.
# # 使用 while 循环来控制迭代次数。
# # The random.randint() function is used to generate random integers.
# # random.randint() 函数用于生成随机整数
# # The modulo operator (%) is used to check for even numbers.
# # 模运算符 (%) 用于检查是否为偶数。
# # The continue statement is used to skip iterations when an even number is generated.
# # continue 语句用于跳过偶数的迭代。
import random
print("Numbers that aren't evenly divisible by 5") #不能被5整除的数字
counter=0
while counter < 10:
    # Get a random number
    number = random.randint(1,999) #Output: Could be any integer between 1 and 999(e.g. , 427,...)
    if int(number /5)==number /5:
        #If it's an evenly divisible by 5, bail out
        #若它能被 5 整除，则退出
        break #Using continue, the output is the same as using break.
    #Otherwise, print it and keep going for a while #否则，打印它并继续一段时间
    print(number)
    #Increment the loop counter.     #增加循环计数器 
    counter +=1
print("Loop is done")
#There's just no way to predict the result because the random number is indeed random and not predictable
#无法预测结果，因为随机数确实是随机的且不可预测
#(which is an  important  concept in many years) #这是多年来的一个重要概念