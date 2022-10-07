"""
    Задание 5
    Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
    из байтовового в строковый тип на кириллице.
"""
import subprocess
import platform
import locale


# args_1 = ['ping', param, '2', 'yandex.ru']
# args_2 = ['ping', param, '2', 'youtube.ru']

args_1 = ['ping', '2', 'yandex.ru']
args_2 = ['ping', '2', 'youtube.ru']


def ping(args):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args.insert(1, param)
    print(args)
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in process.stdout:
        default_encoding = locale.getpreferredencoding()
        line = line.decode(default_encoding).encode('utf-8')
        print(line.decode('utf-8'))


ping(args_1)
ping(args_2)
