# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Мы неабв очень любим Питон иабв Джавабв'
# 'Мы очень любим Питон'

text = 'Мы неабв очень не любим Питон иабв Джавабв абв'
text_find = 'абв'

my_list = text.split()
print(my_list)

# i = 0
# while i in range(len(my_list)):
#     if text_find in my_list[i]:
#         my_list.remove(my_list[i])

#     else:
#         i += 1
# print(my_list)

new_list = [item for item in my_list if text_find not in item]
print(new_list)
