"""
    Задание 4.
    Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
    в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

selection_of_words = ['разработка', 'администрирование', 'protocol', 'standard']
selection_of_words_bytes = []


def converter_to_bytes(elements):
    for elem in elements:
        b_elem = elem.encode('utf-8')
        selection_of_words_bytes.append(b_elem)
        print(f'---\nЭлемент до преобразования: "{elem}". \nПосле преобразования: {b_elem}')


def decode_bytes(elements):
    for elem in elements:
        decode_elem = elem.decode('utf-8')
        print(f'---\nЭлемент в байтовом виде: "{elem}". \nПосле декодирования: {decode_elem}')


print('=========================== ENCODE ===========================')
converter_to_bytes(selection_of_words)
print('=========================== DECODE ===========================')
decode_bytes(selection_of_words_bytes)
