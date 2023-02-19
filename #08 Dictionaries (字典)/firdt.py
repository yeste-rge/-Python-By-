#Python 零基礎新手入門 #08 Dictionaries (字典)
#Item(项目)[Key(键) : Value(值)] Key和Value之间是由冒号所隔阂 而不同Items之间则是由逗号相隔
#注意字典中每个Key都必须是独一无二的
#Dictionary适合拿来储存系统性的资讯
手机 = {
    "厂牌" : "苹果",
    "型号" : "iPhone 14 Pro",
    "容量" : "1 TB",
    "颜色" : "深紫色"
}
#for 规格 in 手机.keys():厂牌 型号 容量 颜色
#for 规格 in 手机.values():苹果 iPhone 14 Pro 1 TB 深紫色
#for 规格 in 手机.items():('厂牌', '苹果') ('型号', 'iPhone 14 Pro') ('容量', '1 TB') ('颜色', '深紫色')
      #print(规格)
for 标题,规格 in 手机.items():
    print(f"{标题}是{规格}")#厂牌是苹果 型号是iPhone 14 Pro 容量是1 TB 颜色是深紫色
#手机.pop("厂牌"){'型号': 'iPhone 14 Pro', '容量': '1 TB', '颜色': '深紫色'}
#手机.popitem() #popitem不需要特别指定key 删除的都是字典中最后一个项目
#{'厂牌': '苹果', '型号': 'iPhone 14 Pro', '容量': '1 TB'}
#手机.clear() {} #clear(删除)的语法 字典中所有类容都会被一次清空
#print(手机)

手机["容量"] = ["128 GB","256 GB","512 GB"]
#print(手机)
#{'厂牌': '苹果', '型号': 'iPhone 14 Pro', '容量': ['128 GB', '256 GB', '512 GB'], '颜色': '深紫色'}
手机["颜色"] = ["深紫色","银色","金色","黑色"]
#print(len(手机["颜色"]))4
#print(手机["颜色"][0])深紫色

#print(手机.ge t("颜色","查无此资讯"))查无此资讯
#if "型号" in 手机:
    #print(手机["型号"])iPhonr 14 Pro
#else:
    #print("查无此资讯")
