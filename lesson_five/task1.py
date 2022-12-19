'''
Напишите программу, удаляющую из файла все слова, содержащие "абв"
'''

def write_file(res):
    with open('file_text.txt', 'w') as data:
        data.write(res)

def del_symbols(file):
    file = list(filter(lambda x: 'абв' not in x, file.split()))
    return " ".join(file)

txt = "абв Напишите абв программу, абв удаляющую из файла абв все слова, абв содержащие \"абв\""
#res_text = del_symbols(txt)
#print(write_file(res_text))
write_file(del_symbols(txt))