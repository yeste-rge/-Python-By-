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
import random
print("Odd numbers")
counter=0
while counter < 10:
    # Get a random number
    number = random.randint(1,999) #Output: Could be any integer between 1 and 999(e.g. , 427,...)
    if int(number /2)==number /2:
        #If it's an even number, don't print it
        continue
    #Otherside, if it's odd, print it and increment the couter.
    print(number)
    #Incorrect the loop counter.
    counter+=1 # if counter=+1 the number will be not stopping
    #柜台
print("Loop is done")