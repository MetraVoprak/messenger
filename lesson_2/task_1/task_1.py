"""
Задание 1
    Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из
    файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

        a) Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и
        считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь
        значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого
        параметра поместить в соответствующий список. Должно получиться четыре списка — например,
        os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для
        хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:
        «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также
        оформить в виде списка и поместить в файл main_data (также для каждого файла);

         b) Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать
         получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий
         CSV-файл;

         c) Проверить работу программы через вызов функции write_to_csv().
"""

from chardet import detect
import re
import csv

collect_data = ['info_1.txt', 'info_2.txt', 'info_3.txt']


def get_data(list_file):
    list_template = [
        r'Изготовитель системы:\s+([a-zA-Z]+)',
        r'Название ОС:\s+([a-zA-Z0-9А-Яа-я\s\.]{1,})[\n]',
        r'Код продукта:\s+([-0-9a-zA-Z]+)',
        r'Тип системы:\s+([-0-9a-zA-Z\s]+)[\n]',
    ]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for name_file in list_file:
        with open(name_file, 'rb') as f:
            content = f.read()
            encoding = detect(content)['encoding']
        with open(name_file, encoding=encoding) as file:
            content = file.read()
        os_prod_list.append(','.join(re.findall(list_template[0], content)))
        os_name_list.append(','.join(re.findall(list_template[1], content)))
        os_code_list.append(','.join(re.findall(list_template[2], content)))
        os_type_list.append(','.join(re.findall(list_template[3], content)))

    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'], [], [], []]

    for i in range(len(os_name_list)):
        main_data[i + 1].append(os_prod_list[i])
        main_data[i + 1].append(os_name_list[i])
        main_data[i + 1].append(os_code_list[i])
        main_data[i + 1].append(os_type_list[i])

    return main_data


def write_to_csv(file_name):
    with open(file_name, 'w') as f_t:
        write_csv = csv.writer(f_t)
        data = get_data(collect_data)
        for i in data:
            write_csv.writerow(i)


write_to_csv('test.csv')
