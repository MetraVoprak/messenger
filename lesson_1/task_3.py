"""
    Задание 3.
    Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

selection_of_words = ['attribute', 'класс', 'функция', 'type']


def converter_to_bytes(elements):
    for elem in elements:
        try:
            bytes_str = f"b'{elem}'"
            eval(bytes_str)
            print(f'Слово "{elem}" можно записать в байтовом типе')
        except SyntaxError:
            print(f'ОШИБКА! Слово "{elem}" невозможно в байтовом типе')


converter_to_bytes(selection_of_words)
