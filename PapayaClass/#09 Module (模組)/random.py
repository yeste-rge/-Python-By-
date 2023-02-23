#Python 零基礎新手入門 #09 Module (模組)
#random随机
#import random
#数字 = [1,2,3,4,5,6]
#random.shuffle(数字) #shuffle(洗牌)函式
#print(数字)

#import random
#数字 = [1,2,3,4,5,6]
#a = random.choice(数字) #choice(选择)
#print(a) 

#import random
#数字 = [1,2,3,4,5,6]
#a = random.randint(10,50)#randint(random integer)的函式
#print(a)
#应用练习:密码产生器
import random
import string #string(模组)它有一些与文字相关的语法
数字 = string.digits #digits可以产生0到9数字
英文 = string.ascii_letters #ascii_letters可以产生英文小写和大写的字母
字母表 = list(数字 + 英文)#用list语法先把它转成清单(list)
random.shuffle(字母表)#shuffle()方法将序列的所有元素随机排序。
长度 = int(input("你的密码要几位数?"))
密码 = "".join(字母表[:长度])#join语法把它转成一般的字串
#密码 = 字母表[:6]#截取出前面6位字母
print(f"你的密码是:{密码}")