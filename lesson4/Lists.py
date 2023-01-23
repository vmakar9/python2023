# s = [10, 20, 30]
# s.append([1, 2])
# print(s)
# s.extend([3, 4])
# print(s)

# s = [10, 20, 30]
# s.insert(1, -5)
# print(s)
# s.insert(1,[1,2])
# print(s)
# s[2:2]=[3,4]
# print(s)
# s[2:3]=[100,200]
# print(s)

# s=[i*(10-i) for i in range(11)]
# print(s)
# print("Видаляємо елемент",s.pop(5))
# print(s)
# s.remove(21)
# print(s)
# del s[3]
# print(s)
# s[2:5]=[]
# print(s)
# s[1:3] = [-1,-2,-3,-4,-5]
# print(s)

# a = [10, 20, 30]
# print("List a:",a)
# b = a
# c= a[:]
# d=a.copy()
# print("List b:",b)
# print("List c:",c)
# print("List d:",d)
# print("Change value of element a[1]=0")
# a[1]=0
# print("List a:",a)
# print("List b:",b)
# print("List c:",c)
# print("List d:",d)

# x= [10,20,[100,200],30,[300,400]]
# y = x[:]
# z = x.copy()
# print("List x:",x)
# print("List y:",y)
# print("List z:",z)
# print("Change value of elements: x[2][1]=0 and x[4]=0")
# x[2][1]=0
# x[4] = 0
# print("List x:",x)
# print("List y:",y)
# print("List z:",z)

# import copy
# A = [[10,20],[[30,40],[50,60]]]
# B = copy.deepcopy(A)
# print("List A:",A)
# print("List B:",B)
# print("Change value of elements A[0][1]=0 and A[1][1][1]=0.")
# A[0][1]=0
# A[1][1][1] = 0
# print("List A:",A)
# print("List B:",B)

# import random
#
# def show(a):
#     n=len(a)
#     print(n,"D-vector: <",sep="",end="")
#     for i in range(n-1):
#         print(a[i],end="|")
#     print(a[n-1],">.",sep="")
# def rand_vector(n):
#     r = []
#     for i in range(n):
#         r.append(random.randint(0,6))
#     return r
# def scal_prod(a,b):
#     Na = len(a)
#     Nb = len(b)
#     N = min(Na,Nb)
#     s = 0
#     for i in range(N):
#         s += a[i]*b[i]
#     return s
# random.seed(2014)
# a = rand_vector(3)
# b= rand_vector(5)
# show(a)
# show(b)
# p = scal_prod(a,b)
# print("Скалярний добуток:",p)

# from random import *
#
# def rand_matrix(n,m):
#     A=[[randint(0,9) for j in range(m)] for i in range(n)]
#     return A
# def unit_matrix(n):
#     A = [[int(i==  j) for i in range(n)] for j in range(n)]
#     return A
# def mult_matrix(A,B):
#     n = len(A)
#     C = [[0 for i in range(n)] for j in range(n)]
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 C[i][j]+=A[i][k]*B[k][j]
#     return C
# def show_matrix(A):
#     for a in A:
#         for b in a:
#             print(b,end=" ")
#         print()
# seed(2014)
# A = rand_matrix(3,5)
# print("List:",A)
# print("Matrix:")
# show_matrix(A)
# E = unit_matrix(4)
# print("Single matrix")
# show_matrix(E)
# A1 = rand_matrix(3,3)
# A2 = rand_matrix(3,3)
# A3 = mult_matrix(A1,A2)
# print("First matrix:")
# show_matrix(A1)
# print("Second matrix:")
# show_matrix(A2)
# print("Multiple matrix:")
# show_matrix(A3)

# a = tuple()
# print(a)
# b = tuple([10,20,30])
# print(b)
# c= tuple("Python")
# print(c)
# a = b+(40,[1,2,3],60)
# print(a)
# print(a[2:5])