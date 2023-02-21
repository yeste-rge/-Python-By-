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

import random
import string #string(模组)它有一些与文字相关的语法
数字 = string.digits #digits可以产生0到9数字
英文 = string.ascii_letters #ascii_letters可以产生英文小写和大写的字母
字母表 = 数字 + 英文
print(字母表)