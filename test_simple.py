# def hello(name):
#     if name == "":
#         print("Hello world!")
#     else:
#         print(f"Hello {name}")


# hello("Sam")
# hello('')            


# def hello2(name):
#     if name:
#         print(f"Hello {name}")
#     else:
#         print("Hello world!")


# hello2([])
# hello2("Sam")


# print("Введиту 2 числа, каждое из которых не больше 10")
# a = int(input("Первое число: "))
# b = int(input("Второе число: "))

# def divide(x, y):
#     if x > 10 or y > 10:
#         result = "число не соответствует требованиям"
#     elif y == 0:
#         result = 'не дели на ноль'
#     else:
#         result = x / y
#     return result

# print(divide(a, b))      


# c = int(input("Введите первое число: "))
# d = int(input("Введите первое второе: "))

# def divide2(x, y):
#     if x > 10 or y > 10:
#         return "Число не соответствует требованиям"
#     if y == 0:
#         return "Не дели на ноль"
#     return x / y

# print(divide2(c, d))

# list1 = [1, 2, 3, 4, 5, 6, 7]

# new_list = []
# for x in list1:
#     new_list.append(x * 2)

# print(new_list)    

# list comprehension

# new_list = [x* 2 for x in list1]

# new_list2 = []
# for x in list1:
#     if x % 2 == 0:
#         new_list2.append(x)

# new_list2 = [x for x in list1 if x % 2 == 0]
# new_list3 = [x for x in list1 if x % 2 != 0]        

# print(new_list) 
# print(new_list2) 
# print(new_list3) 

# i = 0
# while i < 20:
#     print(f"{i + 1}. Hello!")
#     i += 1

# for _ in range(20):
#     print(f"{_ + 1}# Hello!")  

# tupl = ('ont', 'two', 'three')
# # var1 = tupl[0]
# # var2 = tupl[1]
# # var3 = tupl[3]

# var1, var2, var3 = tupl
# print(var2)

def print_text_with_exclamation_at_the_end(text):
    print(f'{text}!')

print_text_with_exclamation_at_the_end('Hi Bro')  

my_print = print_text_with_exclamation_at_the_end

my_print("Fack you, bitch")
