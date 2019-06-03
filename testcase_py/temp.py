#!/usr/bin/python
print ("你好，世界");print("多行用；分开")
#python标识符，字母，数字，下划线，但不能以数字开头，区分大小写
itemone=1;itemtwo=2;itemthree=3
#多行用/分隔，{}[],()直接换行
print(itemone+
      itemtwo+
      itemthree)
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""
""" 此处为注释"""
'''
此处为多行注释
'''

"""
此处为多行注释
"""
import keyword
print(keyword.kwlist)

#数字类型，int,bool, float,complex
#字符串， r"" 让\不转义,代表原始字符，+连接字符串，*重复字符串
#字符串索引，从前是0，从后是-1，变量[头下标:尾下标:步长]

s="thisis a string"
print (s[0:-1])
print(s[2:5])


#input("按下 enter 键后退出。\n")

x="a"
y="b"
print(x,end="")
print(y,end="")

a=b=c=1
x,y,s=1,2,"runoob"
#python 数据类型
# 1. 不可变数据，数字，字符串，元组 2. 可变数据，列表，字典及集合
print(type(x))
print (isinstance(x,str))

del s
del x,y
# + - * / //整除，%取余 **乘方

#列表 变量[头下标:尾下标]，
#inputWords=inputWords[-1::-1] 字符串逆转
#元组，字符串是一种特殊的元组，元组中的元素是不可以改变的，
#集合
headers = {'appId': "MB-STEST-0002", 'appVersion': "2016060401",
           'clientId':"000000000000000-e8206604ed45",'sequenceId':"08002700DC94-15110519074300001",
           'accessToken':"TGTX34LCQSHE1QF2D0GGAHUGSHGT00",'sign':"bd4495183b97e8133aeab2f1916fed41",
           'timestamp':"654323456432434",'language':"zh-cn",'timezone':"8",
           'Content-Type':"application/json",'deviceid':"DC62C2B7BE03DD9C10D07AF23CC8"}
print(headers.keys())
print(headers.values())
print(headers.clear())

#算数运算符 + - * / // % **
#比较运算符 == ！= > < >= <=
#赋值运算符 += -+ *= /+ %= //=
#位运算符 & |  ^ ~ << >>
#逻辑运算符 and or not
#c成员运算符 in  not in
#身份运算符 is is not

#判断语句 if: elif: else:
#循环语句 while语句和for语句 while condition:  while condition : else: 语句  for xx in ss : for xx in ss: else:
# break 跳出循环，continue 跳出本次循环，rang()函数边里序列，rang(5) rang(3,5) range(0,10,3)
# pass 空语句

#迭代器 iter和next


#函数，def 名字():
import  time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

