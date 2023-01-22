# def your_name():
#     print("Hello")
#     name = input("What is your name")
#     return name
#
#
# def say_hello(txt):
#     print("Welcome, ", txt + "!")
#
#
# my_name = your_name()
# say_hello(my_name)

# def my_exp(x, n):
#     s = 0
#     q = 1
#     for k in range(n+1):
#         s += q
#         q *= x/(k+1)
#     return s
# x=1
# for n in range(11):
#     print("n =", n, "-> ", my_exp(x,n))

# def print_text(txt="Значення аргументу за замовчуванням."):
#     print(txt)
#
#
# def show_args(a, b="Другий аргумент не зазначено."):
#     print(a, b)
#
#
# def my_func(x="1-й аргумент x.", y="2-й агрумент y."):
#     print(x, y)
#
#
# print_text("Аргумент вказано явно")
#
# print_text()
#
# show_args("Перший аргумент.", "Другий аргумент")
#
# show_args("Перший аргумент")
#
# my_func()
#
# my_func("Один із аргументів")
#
# my_func(y="Один із аргументів")

# def get_sum(*nums):
#     s = 0
#     for a in nums:
#         s += a
#     return s
#
#
# print(get_sum(1,2,3,4,5))

# def my_func(txt):
#     print("Функція my_func:", txt)
#
# new_func = my_func
# new_func("виклик через new_func")

# def solve_eqn(f, x0, n):
#     x = x0
#     for k in range(1, n + 1):
#         x = f(x)
#     return x
#
#
# def eqn_1(x):
#     return (x ** 2 + 5) / 6
#
#
# def eqn_2(x):
#     return (6*x-5)**0.5
#
# x = solve_eqn(eqn_1,0,10)
#
# print(x)
#
# x = solve_eqn(eqn_2,4,10)
#
# print(x)

# import math
#
#
# def solve_deqn(f, x0, y0, x):
#     n = 1000
#     dx = (x - x0) / n
#     x = x0
#     y = y0
#     for k in range(1, n + 1):
#         y = y + dx * f(x, y)
#         x = x + dx
#     return y
#
#
# def diff_eqn(x, y):
#     return 2 * x - y
#
#
# def y(x):
#     return 2 * (x - 1) * math.exp(-x)
#
#
# h = 0.5
# for k in range(0, 6):
#     x = k * h
#     print("Числовий розв'язок:")
#     print("x =", x, "->  y(x) =", solve_deqn(diff_eqn, 0, 3, x))
#     print("x =", "->  y(x) =", y(x))


# def Fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return Fib(n - 1) + Fib(n - 2)
#
#
# print("Числа Фібоначчі:")
# for i in range(1, 16):
#     print(Fib(i), end=" ")

# def solve(f,x0,n):
#     if n==  0:
#         return  x0
#     else:
#         return solve(f,f(x0),n-1)
#
# def eqn(x):
#     return (x**2+5)/6
# x= solve(eqn,0,10)
#
# print(x)

# def find_value(f,x):
#     print("x =",x,"->  f(x) =", f(x))
#
# my_func = lambda x: 1/(1+x**2)
# find_value(my_func,2.0)
# find_value(lambda x: x*(1-x),0.5)
# z= 1+(lambda x,y: x*y-x**2)(2,3)**2
# print("z = ",z)

# def my_pow(n):
#     return lambda x: x**n
# for n in range(1,4):
#     for x in range(1,11):
#         print(my_pow(n)(x),end=" ")
#     print()

# x=100
# def test_vars():
#     x="локальна змінна"
#     print("У тілі функції x=", x)
# test_vars()
# print("Поза функцією",x)

# def test_vars():
#     print("У тілі функції x=", x)
# x="Глобальна змінна"
# test_vars()
# print("Поза функцією", x)

# x=100
# def test_vars():
#     global x, y
#     print("У тілі функції x =",x)
#     y =200
#     print("У тілі функції y =",y)
#     x=300
# test_vars()
# print("Поза функцією x=", x)
# print("Поза функцією y=", y)

# def factor(mode=True):
#     def sf(n):
#         s = 1
#         i = n
#         while i>1:
#             s *= i
#             i -= 1
#         return s
#     def df(n):
#         s = 1
#         i = n
#         while i>1:
#             s*=i
#             i-= 2
#         return s
#     if mode:
#         return sf
#     else:
#         return df
# print("5! =", factor()(5))
# print("5! =", factor(True)(5))
# print("5!! =", factor(False)(5))

# def factor(mode = True):
#     def f(n, d):
#         s = 1
#         i = n
#         while i>1:
#             s*=i
#             i -=d
#         return s
#     d=1 if mode else 2
#     return lambda n:f(n,d)
# print("5! =", factor()(5))
# print("5! =", factor(True)(5))
# print("5!! =", factor(False)(5))

# def factorial(n):
#     if n==  1:
#         return 1
#     else:
#         return n*factorial(n-1)
# def dfactorial(n):
#     if n==  1 or n== 2:
#         return n
#     else:
#         return n*dfactorial(n-2)
# def factor(mode = True):
#     return factorial if mode else dfactorial
#
# print("5! =", factor()(5))
# print("5! =", factor(True)(5))
# print("5!! =", factor(False)(5))

def D(f):
    def df(x,dx=0.001):
        return (f(x+dx)-f(x))/dx
    return df
def f1(x):
    return x**2
def f2(x):
    return 1/(1+x)
def show(F,Nmax,Xmax,dx,f):
    for i in range(Nmax+1):
        x = i*Xmax/Nmax
        print(F(x),F(x,dx),f(x),sep=" ->  ")
F1 = D(f1)
F2 = D(f2)

print("Похідна (x**2)'=2x:")
show(F1,5,1,0.01,lambda x: 2*x)
print("Похідна (1/(1+x)'=-1/(1+x)**2:")
show(F2,5,1,0.01,lambda x: -1/(1+x)**2)
