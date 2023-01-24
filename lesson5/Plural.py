# A = [1, 30, "text", True, 30, 100, False]
# print("List A:",A)
# B = set(A)
# print("Plural B:",B)
# C= {1,30,"text",True,30,100,False}
# print("Plural C:", C)
# print("Equals plural:", B== C)
# print("Element 1 in plural C:", 1 in C)

# A ={1,2,3,4}
# print("Plural A:",A)
# B = {3,4,5,6}
# print("Plural B:",B)
# C = A|B
# print("Plural C=A|B:",C)
# print("Plural A.union(B):",A.union(B))
# print("Plural B.union(A):",B.union(A))
# A.update(B)
# print("Plural A:",A)
# B = B | {-1,-2,-3}
# print("Plural B:",B)
# C|={7,8,9}
# print("Plural C:",C)

# A = {1,2,3,4}
# print("Plural A:", A)
# B = {3,4,5,6}
# print("Plural B:", B)
# C = A&B
# print("Plural C = A & B:", C)
# print("Plural A.intersection(B):",A.intersection(B))
# print("Plural B.intersection(A):",B.intersection(A))
# A.intersection_update(B)
# print("Plural A:",A)
# B = B&{4,6,8,10}
# print("Plural B:",B)
# C &= {1,2,3}
# print("Plural C:",C)

# A = {1,2,3,4}
# print("Plural A:",A)
# B = {3,4,5,6}
# print("Plural B:",B)
# C = A-B
# print("Plural C:",C)
# print("Plural A.difference(B):",A.difference(B))
# print("Plural B.difference(A):", B.difference(A))
# A.difference_update(B)
# print(A)
# B = B-{4,6,8,8,10}
# print("Plural B:",B)
# C -={1,3,5}
# print("Plural C:",C)

# A= {1,2,3,4}
# print("Plural A:",A)
# B = {3,4,5,6}
# print("Plural B:",B)
# C= A^B
# print("Plural C:",C)
# print("Plural A.symmetric_difference(B):",A.symmetric_difference(B))
# print("Plural B.symmetric_difference(A):",B.symmetric_difference(A))
# A.symmetric_difference_update(B)
# print("Plural A:",A)
# B = B^{4,6,8,10}
# print("Plural B:",B)
# C^={1,3,5}
# print("Plural C:",C)

# n = 100
# E = {s for s in range(1,n+1)}
# A1= {s for s in E if s%5== 2}
# A2 = {s for s in E if s%5 ==  4}
# A = A1|A2
# B = {s for s in E if s%7 ==  3}
# C = {s for s in E if s%3 ==  1}
# D = (A&B) -C
# print("Наведені нижче числав від 1 до", n)
# print("1) при діленні на 5 дають в остачі 2 або 4;")
# print("2) при діленні на 7 дають в остачі 3")
# print("3) при діленні на 3 не дають в остачі 1:")
# print(D)

# n = 100
# D = {s for s in range(1,n+1) if (s%5 == 2 or s%5 ==  4) and s% 7 ==  3 and s%3!=  1}
# print("Наведені нижче числав від 1 до", n)
# print("1) при діленні на 5 дають в остачі 2 або 4;")
# print("2) при діленні на 7 дають в остачі 3")
# print("3) при діленні на 3 не дають в остачі 1:")
# print(D)

# n = 100
# D = set()
# for s in range(1,n+1):
#     if s%5 ==  2 or s% 5 ==  4:
#         if s% 7 ==  3:
#             if s%3!=  1:
#                 D.add(s)
# print("Наведені нижче числав від 1 до", n)
# print("1) при діленні на 5 дають в остачі 2 або 4;")
# print("2) при діленні на 7 дають в остачі 3")
# print("3) при діленні на 3 не дають в остачі 1:")
# print(D)

# A = [["Шевченко T.Г.","Кобзар"],["Франко І.Я.","Лис Микита"],["Сковорода Г.С.","Сад божественних пісень"]]
# writers = dict(A)
# print("Dictionary:")
# print(writers)
# print("Франко написав казку:",writers["Франко І.Я."])
# writers["Франко І.Я."] = "Украдене щастя"
# print("Dictionary after change of element:")
# print(writers)
# writers["Костенко Л.В"] = "Записи українського самашедшого"
# print("Dictionary after add of element:")
# print(writers)
# print()
# print("Autors and their creation")
# for s in writers.keys():
#     print("Autor:",s)
#     print("Creation:", writers[s])
#     print()
# lights = dict(червоне ="рух заборонено", жовте = " увага", зелене = "рух дозволено")
# print("New dictionary")
# print(lights)
# color ="зелене"
# print("Якщо горить", color,"світло, то", lights[color]+ "!")
# print()
# girls = {(90,60,90):"Світлана", (85,65,89):"Юля",(92,58,91):"Ніна"}
# params = (90,60,90)
# print("Another one dictionary")
# print(girls[params]+":",params)

# symbs = dict([["a","first"],["b","second"]])
# more_syms = dict([["c","third"],["d","fourth"]])
# symbs.update(more_syms)
# print("Dictionary:",symbs)
# print("Count of element in dictionary", len(symbs))
# print("Element with key 'c':",symbs.get("c","this key dont exist"))
# print("Element with key 'c' exist", "c" in symbs)
# del symbs["c"]
# print("Dictionary:",symbs)
# print("Element with key 'c':",symbs.get("c","this key dont exist"))
# print("Element with key 'c' exist", "c" in symbs)
# print("Keys of dictionary:",list(symbs.keys()))
# print("Value elements of dictionary",list(symbs.values()))
# print("Contens dictionary",list(symbs.items()))
# print("Deleting element with value" , symbs.pop("b"))
# print("Dictionary:", symbs)
# symbs.clear()
# print("Dictionary:",symbs)

# txt = "Knowledge language 'Python'- quarantee success"
# print(txt)
# txt = 'Knowledge language "Python"- quarantee success'
# print(txt)
# txt = 'Knowledge language \"Python\"- quarantee success'
# print(txt)
# txt = 'Knowledge language \'Python\'- quarantee success'
# print(txt)
# txt = "Knowledge language 'Python'\n- quarantee success"
# print(txt)
# txt = """Knowledge language "Python"- quarantee success"""
# print(txt)

# txt ="We learning " "Python"
# print(txt)
# print("Average",len(txt),"letters")
# print("Index\tletter")
# for i in range(len(txt)):
#     print(str(i)+": \t"+txt[i])
# print(txt[12:])
# print(txt[::-1])
# word = "Java"
# txt = txt[:3]+"not"+txt[2:12]+word
# print(txt)

# txt ="We learning " "Python"
# print(txt.upper())
# print(txt.lower())
# print(txt.capitalize())
# print(txt.title())
# print(txt.swapcase())
# print(txt)

# txt ="""В.С. Стус. "Сто років..." (уривок):
# Сто років як сконала Січ.
# Сибір. І соловецькі келії.
# І глупа облягає ніч
# Пекельний край і крик пекельний
# Сто років Мучених надій
# І оповідань , і вір , і крові.
# Синів, що за любов тавровані
# Сто серць, як сто палахкотінь"""
# word ="Сто"
# print(txt,end='\n\n')
# print("Підрядок зустрічається",txt.count(word),"рази")
# print("Перша позиція:", txt.index(word))
# print("Наступна позиція",txt.find(word,13))
# print("Остання позиція:",txt.rindex(word))
# print("На початку ініціали:",txt.startswith("В.С."))
# print("У кінці крапка:",txt.endswith("."),end='\n\n')
# print(txt.replace(" ","_"))

# print("123".isdigit(),"12.3".isdigit())
# print("abc".isalpha(),"abc123".isalpha())
# print("ab12".isalnum(),"ab12\n".isalnum())
# print("ABC".isupper(),"aBc".isupper())
# print("abc".islower(),"aBc".islower())
# print("Ab12 Ab12".istitle(),"Ab12 AB12".istitle())

# txt="_*_ABC_*_abc_*_"
# print(txt.lstrip("_*_"))
# print(txt.rstrip("_*_"))
# print(txt.strip("_*_"))
# print(txt.split("*"))
# print(txt.rsplit("*"))
# print(txt.partition("*"))
# print(txt.rpartition("*"))
# print("abc \n ABC \n ***".splitlines())
# print("_*_".join(["AAA","BBB","CCC"]))

# txt ="ABCDEFGH"
# print("*"+txt.center(20)+"*")
# print("*"+txt.rjust(20)+"*")
# print("*"+txt.ljust(20)+"*")

# txt = "{0} по {0} - буде {1}"
# print(txt.format("два","чотири"))
# print(txt.format("три","чотири"))
# print("Текст '{0}': {0:<20}.".format("abcdef"))
# print("Текст '{0}': {0:^20}.".format("abcdef"))
# print("Текст '{0}': {0:>20}.".format("abcdef"))
