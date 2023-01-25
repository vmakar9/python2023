# class MyClass:
#     def say_hello(self):
#         print("Hello World")
# obj = MyClass()
# obj.say_hello()

# class MyClass:
#     def set(self,n):
#         print("Set number")
#         self.number = n
#     def get(self):
#         print("Value field:",self.number)
# obj =MyClass()
# obj.set(100)
# obj.get()

# class MyClass:
#     pass
#
# obj = MyClass()
# obj.number = 100
# print(obj.number)

# class MyClass:
#     def __init__(self):
#         self.number = 0
#         print("Created specimen of class")
# obj = MyClass()
# print("Value of field", obj.number)

# class MyClass:
#     def set(self,n):
#         self.num = n
#     def get(self):
#         print("Value of field:",self.num)
#     def __init__(self,n=0):
#         self.set(n)
#         print("Created specimen of class")
#         self.get()
# a = MyClass()
# b = MyClass(100)

# class MyClass:
#     def __init__(self):
#         print("Hello")
#     def __del__(self):
#         print("Bye")
# obj = MyClass()
#
# del obj

# class MyClass:
#     name ="Class MyClass"
#     def set(self,n):
#         self.nickname = n
#     def get(self):
#         print("Value of field",self.nickname)
#     def __init__(self,n):
#         self.set(n)
#         print("Specimen of class")
#         self.get()
# green = MyClass("green")
# print("Included",green.name)
#
# red = MyClass("red")
# print("Included",red.name)
#
# MyClass.name = "Here maybe was your add"
# print("Asks Red",red.name)
# print("Asks Green", green.name)

# class MyClass:
#     name = "Class MyClass"
#     def set(self,n):
#         self.nickname = n
#     def get(self):
#         print("Value of field:",self.nickname)
#     def __init__(self,n):
#         self.set(n)
#         print("Created Specimen of class")
#         self.get()
# green = MyClass("green")
# print("Depends:",green.name)
# red = MyClass("red")
# print("Depends:",red.name)
# green.name = "This was be green"
# print("Red asks",red.name)
# print("Green asks",green.name)
# MyClass.name = "Here maybe was your add"
# print("Asks Red",red.name)
# print("Asks Green", green.name)
# del green.name
# print("Asks Green", green.name)

# class MyClass:
#     pass
# A = MyClass()
# B = MyClass()
# A.first = "Specimen A"
# B.second = "Specimen B"
# MyClass.total = "Class MyClass"
# print(A.total,"-> ",A.first)
# try:
#     print(A.second)
# except AttributeError:
#     print("There is no field in specimen A")
# try:
#     print(B.first)
# except AttributeError:
#     print("There is no field in specimen B")
#
# del MyClass.total
#
# try:
#     print(A.total)
# except AttributeError:
#     print("There is no field in Specimen A")
#
# try:
#     print(B.total)
# except AttributeError:
#     print("There is no field in Specimen B")
#
# del A.first
#
# try:
#     print(A.first)
# except AttributeError:
#     print("There is no field in Specimen A")
#
#

# class MyClass:
#     def say(self):
#         print("Everyone hello")
# obj = MyClass()
# obj.say()
# MyClass.say(obj)
# MyClass.say("Some text")

# class MyClass:
#     pass
# A = MyClass()
# B = MyClass()
# C = MyClass()
# def hello():
#     print("Method Spicemen - `hello`")
# def hi():
#     print("Another one method - `hi`")
# A.say = hello
# C.say = hi
# A.say()
# try:
#     B.say()
# except AttributeError:
#     print("There is no method")
# C.say()
# try:
#     MyClass.say()
# except AttributeError:
#     print("There is no function")
# del A.say
# try:
#     A.say()
# except AttributeError:
#     print("There is no method")
# C.say()

# class MyClass:
#     def __init__(self,n):
#         self.name = n
# A = MyClass("A")
# B = MyClass("B")
# def hello(self):
#     print("This is Specimen",self.name,"- hello")
# def hi(self):
#     print(self.name+": hi")
# MyClass.say = hello
# A.say()
# B.say()
# MyClass.say(A)
# MyClass.say(B)
# MyClass.say = hi
# A.say()
# B.say()
# MyClass.say(A)
# MyClass.say(B)
# del MyClass.say
# try:
#     A.say()
# except AttributeError:
#     print("There is no method")
# try:
#     B.say()
# except AttributeError:
#     print("There is no method")
# try:
#     MyClass.say(A)
# except AttributeError:
#     print("There is no function")

# from copy import  copy,deepcopy
# class MyClass:
#     def __init__(self,name,nums):
#         self.name = name
#         self.nums = nums
#     def show(self):
#         print("name -> ",self.name)
#         print("nums -> ",self.nums)
# x = MyClass("Python",[1,2,3])
# print("Specimen x:")
# x.show()
# y = copy(x)
# z = deepcopy(x)
# print("Specimen y:")
# y.show()
# print("Specimen z:")
# z.show()
# print("Field specimen x changing")
# x.name = "Java"
# x.nums[0] = 0
# print("specimen x:")
# x.show()
# y.show()
# z.show()

# class ComplNum:
#     def __init__(self,x=0,y=0):
#         if type(x) ==  ComplNum:
#             self.Re = x.Re
#             self.Im = x.Im
#         else:
#             self.Re = x
#             self.Im = y
#     def show(self):
#         print("Re =",self.Re)
#         print("Im =",self.Im)
# a = ComplNum(1,2)
# b = ComplNum(a)
# print("Specimen a:")
# a.show()
# print("Specimen b:")
# b.show()
# print("Field Specimen a changing")
# a.Re = 10
# a.Im = 20
# print("Specimen a")
# a.show()
# print("Specimen b")
# b.show()

class MyClass:
    def __init__(self,arg,nums=None):
        if type(arg) ==  MyClass:
            self.name = arg.name[:]
            self.nums = arg.nums[:]
        else:
            self.name = arg
            self.nums = nums
    def show(self):
        print("name -> ",self.name)
        print("nums -> ",self.nums)
x = MyClass("Python",[1,2,3])
print("Specimen x:")
x.show()
y = MyClass(x)
y.show()
print("Field specimen x changing")
x.name = "Java"
x.nums[0] = 0
print("Specimen x:")
x.show()
print("Specimen y:")
y.show()




