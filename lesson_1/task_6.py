"""
    Задание 6
    Создать текстовый файл test_file.txt, заполнить его тремя строками:
    «сетевое программирование», «сокет», «декоратор».
    Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

from chardet import detect

text = ['сетевое программирование', 'сокет', 'декоратор']


def check_encoding(name_file, content_file):
    with open(name_file, 'w', encoding='utf-8') as f:
        for line in content_file:
            f.write(line + '\n')

    with open(name_file, 'rb') as f:
        content = f.read()
    encoding = detect(content)['encoding']
    print('encoding: ', encoding)

    with open(name_file, encoding=encoding) as file:
        for str_file in file:
            print(str_file, end='')


check_encoding('test_file.txt', text)
