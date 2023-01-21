# res = eval(input("Input something: "))
# if type(res) == int:
#     print("This is integer")
# else:
#     print('This is not integer')
#
# print("Work is done")

# res = eval(input("Input something: "))
# resType = type(res)
# if resType == int:
#     print("This is integer")
# if resType ==  float:
#     print("This is valid number")
# if resType !=  int and resType !=  float:
#     print("Maybe this is text")
# print("Work is done")

# res = eval(input("Input something: "))
# resType = type(res)
# if resType ==  int:
#     print("This is integer")
# elif resType ==  float:
#     print("This is valid number")
# else:
#     print("Maybe this is text")
# print("Work is done")

# print("Sum int numbers")
# n = 100
# text = "1+2+3...+" + str(n) + " ="
# i = 1
# s = 0
# while True:
#     s += i
#     i += 1
#     if i > n:
#         break
# print(text, s)

# n = 500
# dz = 1 / n
# pts = 0
# i = 0
# while i<= n:
#     x = dz *i
#     j =0
#     while j<= n:
#         y = dz*j
#         if x >= y >= x**2:
#             pts = pts + 1
#         j = j+1
#     i = i+1
# s = pts/(n+1)**2
# print("Площа фігури: ",s)

# print("Sum int numbers")
# n = 100
# text = "1+2+...+" + str(n) + " ="
# s = 0
# for i in range(1, n + 1):
#     s = s + i
# print(text, s)

# txt ="Python"
# i =1
# for s in txt:
#     t = str(i) + "-a letter:"
#     print(t,s)
#     i=i+1
# print("Work is done")

# print("Перевіряємо вміст списку: ")
# #myList = [1, 3 + 2j, True, 4.0]
# myList = [1, 3 + 2j, "Python", 4.0]
# print("Список:",myList)
# for s in myList:
#     if type(s) ==  str:
#         print("У списку э текстові елементи!")
#         break
#     else:
#         print("У списку немаэ текстових елементів")

# print("Пошук елементів, які збігаються.")
# A = [2, False, 9.1, 2 - 1j, "hello", 5, "Python"]
# B = [5, 3, "HELLO", 7, 12.5, "Python", True, False]
# print("fist list: ", A)
# print("second list: ", B)
# print("Збігаються:")
# i = 0
# for a in A:
#     i = i + 1
#     j = 0
#     for b in B:
#         j = j + 1
#         if a == b:
#             txt = str(i) + "-й елемент із 1-го списку"
#             txt = txt + str(j) + "-й елемент із 2-го списку"
#             print(txt)
# print("Пошук закінчено")

# print("ax = b")
# try:
#     a = float(input("Input a: "))
#     b = float(input("Input b:"))
#     x = b / a
#     print("x = ", x)
# except:
#     print("Wrong input information")
# print("Work is done")

# print("ax = b")
# try:
#     a = float(input("Input a: "))
#     b = float(input("Input b: "))
#     x = b/a
#     print("x = ", x)
# except ValueError:
#     print("Number need")
# except ZeroDivisionError:
#     print("You cant divide on zero")
# print("Work is done")
