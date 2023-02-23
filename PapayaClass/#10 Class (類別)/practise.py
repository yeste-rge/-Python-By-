#Python 零基礎新手入門 #10 Class (類別)
import random
class 游戏角色: #Class名称如果你要使用英文一般命名的规范是采用首字大写的规则 #class GameCharacter
    生命值 = 400 # ←游戏在刚开始的时候所有角色都会有一些共同⌈属性⌋
    def __init__(self,姓名): #__init__(initialize(初始化)的缩写)
        self.姓名 = 姓名
    def 防御(self,指令):
        if 指令 == 1:
            print(f"{self.姓名}摆出了格挡姿势 ~") 
            return 0.5
        elif 指令 == 2:
            print(f"{self.姓名}尝试闪避攻击 ~")
            return random.choice([0.3,1]) #random模组.choice函式
class 战士(游戏角色):
    def 攻击(self,指令):
        if 指令 == 1:
         print(f"{self.姓名}使出了突刺攻击!!")
         return 200
        elif 指令 == 2:
            print(f"{self.姓名}奋力使出了迥旋辉砍!!")
            return random.choice([300,100])
class 魔物(游戏角色):
    def 攻击(self,指令):
        if 指令 == 1:
         print(f"{self.姓名}使出了利爪攻击!!")
         return 200
        elif 指令 == 2:
            print(f"{self.姓名}张出血口喷了毒液!!")
            return random.choice([300,100])
玩家姓名 = input("请输入你的姓名:")
玩家 = 战士(玩家姓名)
敌方 = 魔物("哥布林")
随机 = random.choice([1,2])
while True:
    攻击指令 = int(input("请输入您的攻击指令(1)普通攻击(2)特殊攻击:"))
    玩家攻击力 = 玩家.攻击(攻击指令)
    损血 = int(敌方.防御(随机) * 玩家攻击力)
    敌方.生命值 -= 损血
    if 敌方.生命值 <= 0:
        print(f"{敌方.姓名}倒下了,{玩家.姓名}胜利!!")
        break
    else:
        print(f"{敌方.姓名}受到了{损血}伤害,生命值剩下 {敌方.生命值}")
        print("")

        攻击指令 = int(input("请输入您的攻击指令(1)普通攻击(2)特殊攻击:"))
 
    
    防御指令 = int(input("请输入您的攻击指令(1)格挡(2)闪退:"))
    敌方攻击力 = 敌方.攻击(随机)
    损血 = int(玩家.防御(防御指令) * 敌方攻击力)
    玩家.生命值 -= 损血
    if 玩家.生命值 <= 0:
        print(f"{玩家.姓名}受伤过重倒下了,游戏结束 ~")
        break
    else:
        print(f"{玩家.姓名}受到了{损血}伤害,生命值剩下 {玩家.生命值}")
        print("")