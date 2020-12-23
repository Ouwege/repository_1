# def calculator(a,b):
#     l=["+","-","*","/"]
#     if isinstance(a,float) and isinstance(b,float):
#         for i in range(4):
#             if l[i]=='+':
#                 print('%.2f+%.2f=%.2f' % (a,b,a+b))
#             elif l[i]=='-':
#                 print('%.2f-%.2f=%.2f' % (a, b, a - b))
#             elif l[i]=='*':
#                 print('%.2f*%.2f=%.2f' % (a, b, a * b))
#             else:
#                 if b==0:
#                     print('除数不能为零')
#                 else:
#                     print('%.2f/%.2f=%.2f' % (a, b, a / b))
# a=float(input('输入第一个数：'))
# b=float(input('输入第二个数：'))
# print('加减乘除结果为：')
# calculator(a,b)

# list=[]
# for no in range(1,61):
#     list.append('%d号'%no)
# print(list)

# print('好好学习，天天向上')

# while 1:
#     try:
#         a=float(input('请输入数字a:'))
#         b=float(input('请输入数字b:'))
#     except Exception:
#         print('输入不合法！')
#     else:
#         if a>b:
#             print('a大于b')
#         elif a<b:
#             print('a小于b')
#         else:
#             print('a等于b')

# class Person:
#     def __init__(self,age,name,gender,grade):
#         self.age=age
#         self.name=name
#         self.gender=gender
#         self.grade=grade
# p=Person(20,'张三','男','大二')
# print(p.name,p.gender)

# list_1=[1,'2','adf',[1,'3'],False,'2']
# tuple_1=(2,'Davie',9.8,True,['apple','banana'],2)
# set_1={1,2,2,'abc','def','abc'}
# dict_1={'a':'apple','b':'banana','c':'cat'}
# print(list_1)
# print(tuple_1)
# print(set_1)
# print(dict_1)

# def print100():
#     list=[]
#     for i in range(1,101,2):
#         list.append(i)
#     print(list)
# print100()

# def getColor(s):
#     if s=='红':
#         print('red')
#     elif s=='黄':
#         print('yellow')
#     elif s=='蓝':
#         print('blue')
#     elif s=='绿':
#         print('green')
#     else:
#         print('输入不正确！')
# getColor(input('输入颜色（红、黄、蓝、绿）：'))
#
# def checkTem(a):
#     if a>=38.5:
#         print('温度过高！')
#     elif a>35 and a<38.5:
#         print('体温正常')
#     else :
#         print('体温过低！')
# while 1:
#     checkTem(float(input('当前温度：')))

# sum=0
# for i in range(1,11):
#     sum+=i
# print('1-10的和为：',sum)

# def func1():
#     pass
# def func2():
#     return 1
# print('调用第一个函数的结果为：',func1())
# print('调用第二个函数的结果为：',func2())

# set_1={'Hello',520,False,99.9}
# for item in set_1:
#     print(item)

class Store:
    def __init__(self,drink,bread,toothpaste,icecream):
        self.drink=drink
        self.bread=bread
        self.toothpaste=toothpaste
        self.icecream=icecream
    def show(self):
        print('饮料有：',self.drink)
        print('面包有：',self.bread)
        print('牙膏有：',self.toothpaste)
        print('雪糕有：',self.icecream)
# shop=Store(['菊花茶','东鹏特饮'],['铜锣烧','豆沙包'],['黑妹牙膏','黑人牙膏'],'五羊牌雪糕')
class Shop(Store):
    def __init__(self,goods):
        self.goods=goods
    def show(self):
        print('生活用品有：',self.goods)
shop=Shop(['水桶','毛巾','扫把'])
shop.show()
