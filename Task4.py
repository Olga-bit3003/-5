# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
with open('text1.txt', 'w') as data:
    data.write('LLLLLLLLLLWWWWWWLLLLLBBBBBLWWWWWWWWWWJJJJJJJJJJ')

with open('text2.txt', 'r') as data:
    string = data.readline()

def rle_text1(text2_string):
    text1_string = ''
    count = 1
    char = text2_string[0]
    for i in range(1, len(text2_string)):
        if text2_string[i] == char:
            count += 1
        else:
            text1_string = text1_string + str(count) + char
            char = text2_string[i]
            count = 1
            text1_string = text1_string + str(count) + char
    return text1_string


def rle_text2(text1_string):
    text1_string = ''
    char_amount = ''
    for i in range(len(text1_string)):
        if text1_string[i].isdigit():
            char_amount += text1_string[i]
        else:
            text2_string += text1_string[i] * int(char_amount)
        char_amount = ''
    print(text2_string)

    return text2_string


with open('text1.txt', 'r') as file:
    text2_string = file.read()

with open('text2.txt', 'w') as file:
    text1_string = rle_text1(text2_string)
    file.write(text1_string)

print('text2 string: \t' + text2_string)
print('text1 string: \t' + rle_text1(text2_string))
print(f'Compress ratio: \t{round(len(text2_string) / len(text1_string), 1)}')