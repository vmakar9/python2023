# print("Давайте познайомимося!")
# name = input("Як вас звати?")
# print("Доброго дня,", name+"!")

# a = (5+2)**2-3*2
# b = 6-5/2
# c = 10//4 +10%3
# print(a,b,c)

# a = "(5+2)**2-3*2"
# b = "6-5/2"
# c = "10//4 +10%3"
# print(a+" =", eval(a))
# print(b+" =", eval(b))
# print(c+" =", eval(c))

# a = 70>>3
# b= ~a
# c=a<<1
# print(a,b,c)
# print(7|3,7&3,7^3)

# a= True
# b = not a
# print(a,b)
# c = a and b
# d = a or b
# print(c,d)

# x = 10
# y = 20
# z = x and y
# print(z)
# z = x or y
# print(z)
# print(not x)

# a = 100
# b = 200
# print(a < b, a >= b, a == 100, b != 199)

a = float(input("Input first number: "))
b = float(input("Input second number: "))
value_1 = "First number greater more that second"
value_2 = "Second number dont lower that first"
res = value_1 if a > b else value_2
print(res)
