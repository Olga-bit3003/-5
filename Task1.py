#Напишите программу, удаляющую из текста все слова, содержащие ""абв""
text =('Жила абв абв была абв в лесу  абв')


def del_obi_name(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = del_obi_name(text)
print(text)