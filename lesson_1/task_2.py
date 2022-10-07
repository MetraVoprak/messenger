"""
    Задание 2.
    Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
    (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""

selection_of_words = ['class', 'function', 'method']


def converter_to_bytes(elements):
    for elem in elements:
        bytes_str = f"b'{elem}'"
        result = eval(bytes_str)
        print(f'Тип данных: {type(result)}. Содержимое: {result}, длинна переменно: {len(result)}')


converter_to_bytes(selection_of_words)
