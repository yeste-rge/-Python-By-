class 游戏角色: #Class名称如果你要使用英文一般命名的规范是采用首字大写的规则 #class GameCharacter
    等级 = 1 # ←游戏在刚开始的时候所有角色都会有一些共同⌈属性⌋
    经验值 = 0#←↓
    def __init__(self,姓名,年龄): #__init__(initialize(初始化)的缩写)
        self.姓名 = 姓名
        self.年龄 = 年龄
    def 冲锋(self):#Self-代表目前的游戏角色
        print(f"{self.姓名}一个弓步冲向了敌人!")
    def 洞察(self):
        print(f"{self.姓名}用敏锐眼光环顾着四周")
class 战士(游戏角色):
    def 攻击(self):
        print(f"{self.姓名}使出了攻击!!")