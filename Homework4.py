# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# text = input()
# text = text.split()
# new_text = list(filter(lambda i: 'абв' not in i, text))
# print(new_text)


# Создайте программу для игры в ""Крестики-нолики"".
# Игра в крестики нолики с человеком 

# from nis import maps

# import symbol


# maps = [1,2,3,
#         4,5,6,
#         7,8,9]

# victories = [[0,1,2],
#              [3,4,5],
#              [6,7,8],
#              [0,3,6],
#              [1,4,7],
#              [2,5,8],
#              [0,4,8],
#              [2,4,6]]

# def print_maps():
#     print(maps[0], end = " ")
#     print(maps[1], end = " ")
#     print(maps[2])

#     print(maps[3], end = " ")
#     print(maps[4], end = " ")
#     print(maps[5])

#     print(maps[6], end = " ")
#     print(maps[7], end = " ")
#     print(maps[8])

# def step_maps(step,symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol

# def get_result():
#     win = ""

#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps [i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps [i[2]] == "O":
#             win = "O"
#     return win

# game_over = False
# player1 = True

# while game_over == False:

#     print_maps()

#     if player1 == True:
#         symbol = "X"
#         step = int(input("Человек 1, сделайте ход: "))
#     else:
#         symbol = "O"
#         step = int (input("Человек 2, ваш ход: "))
    
#     step_maps(step,symbol)
#     win = get_result()
#     if win != "":
#         game_over = True
#     else:
#         game_over = False
#     player1 = not(player1)

# print_maps()
# print("Победил: ", win)

###################################################
# Игра с компьютером 


# maps = [1,2,3,
#         4,5,6,
#         7,8,9]
 
# victories = [[0,1,2],
#              [3,4,5],
#              [6,7,8],
#              [0,3,6],
#              [1,4,7],
#              [2,5,8],
#              [0,4,8],
#              [2,4,6]]
 
# def print_maps():
#     print(maps[0], end = " ")
#     print(maps[1], end = " ")
#     print(maps[2])
 
#     print(maps[3], end = " ")
#     print(maps[4], end = " ")
#     print(maps[5])
 
#     print(maps[6], end = " ")
#     print(maps[7], end = " ")
#     print(maps[8])
     

# def step_maps(step,symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol
 
# def get_result():
#     win = ""
 
#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"   
             
#     return win
 
# def check_line(sum_O,sum_X):
 
#     step = ""
#     for line in victories:
#         o = 0
#         x = 0
 
#         for j in range(0,3):
#             if maps[line[j]] == "O":
#                 o = o + 1
#             if maps[line[j]] == "X":
#                 x = x + 1
 
#         if o == sum_O and x == sum_X:
#             for j in range(0,3):
#                 if maps[line[j]] != "O" and maps[line[j]] != "X":
#                     step = maps[line[j]]
                 
#     return step
 

# def MI():        
#     step = ""
#     step = check_line(2,0)
#     if step == "":
#         step = check_line(0,2)        
#     if step == "":
#         step = check_line(1,0)           
#     if step == "":
#         if maps[4] != "X" and maps[4] != "O":
#             step = 5           
#     if step == "":
#         if maps[0] != "X" and maps[0] != "O":
#             step = 1           
#     return step
 
# game_over = False
# human = True
 
# while game_over == False:
 
#     print_maps()
 
#     if human == True:
#         symbol = "X"
#         step = int(input("сделайте ход: "))
#     else:
#         print("программа сделала свой ход: ")
#         symbol = "O"
#         step =  MI()
#     if step != "":
#         step_maps(step,symbol) 
#         win = get_result() 
#         if win != "":
#             game_over = True
#         else:
#             game_over = False
#     else:
#         print("Ничья!")
#         game_over = True
#         win = "ничья"
 
#     human = not(human)        
        
# print_maps()
# print("решение игры:", win)   

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# with open('text_doc.text', 'w', encoding='UTF-8') as textfile:
#     textfile.write(input('введите текст для сжатия: '))
# with open('text_doc.text', 'r') as textfile:
#     my_text =textfile.readline()
#     text_compr = my_text.split()

#     print(my_text)

#     def text_file(text):
#         file = ''
#         prev_char = ''
#         count = 1
#         if not text:
#             return ''

#         for char in text:
#             if char != prev_char:
#                 if prev_char:
#                     file += str(count) + prev_char
#                 count = 1
#                 prev_char = char
#             else:
#                 count += 1
#         else:
#             file += str(count) + prev_char
#             return file

# text_compr = text_file(my_text)

# with open('text_code_words.txt', 'w', encoding='UTF-8') as file:
#     file.write(f'{text_compr}')
# print(text_compr)