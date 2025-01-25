import os
import time
import random
import itertools
import psutil
import colorama
from colorama import Fore, Style
os.system('TITLE SmartTool')
os.system('color E')


# pyinstaller --onefile SmartTool.py

print('         _  _   _  _    __          _____    _   _    _____   _  _    __')
print('        | \\/ |  \\\\//   /  \\   |_   |_   _|  | | / |  |_   _|  \\\\//   /  \\')
print('        | || |   //   / /\\ \\  | |    | |    | |/| |    | |     //   / /\\ \\')
print('        |_||_|  //   /_/  \\_\\ |_/    |_|    |_/ |_|    |_|    //   /_/  \\_\\')
print('\n             "mrt"    - проверка ПК систепой windows')
print('             "shell"    - папка с автозагрузкой')
print('             "shutdown" - безопасное выключение ПК')
print('             "shutup"   - безопасная перезагрузка ПК')
print('             "shutoff"  - отмена выключения/перезагрузки ПК')
print('             "CPU"      - посмотреть нагрузку цп')
print('             "folder"   - посмотреть содержимое папки')
print('             "search"   - поиск в интернете')
print('             "DISK"     - посмотреть память на диске')
print('             "anim"     - воспроизвести анимацию')
print('             "cmd"     - написать команду для cmd')
while True:
    os.system('color E')
    #os.system('cls')
    comand = input('>>> ')
    #полезно ━━━━━━━━



    if comand == 'mrt':
        os.system('mrt')

    elif comand == 'shell':
        os.system('start C:\\Users\\%USERNAME%\\AppData\\Roaming\\Microsoft\\Windows')

    elif comand == 'shutdown':
        os.system('shutdown /s /t 30 /c "Сеанс будет завершен через 30 c. Действие совешено программой "SmartTool""')

    elif comand == 'shutup':
        os.system('shutdown /r /t 30 /c "Сеанс будет перезагружен через 30 c. Действие совешено программой "SmartTool""')

    elif comand == 'shutoff':
        os.system('shutdown /a')

    elif comand == "CPU" or comand == "Cpu" or comand == "CpU" or comand == "CPu" or comand == "cPu" or comand == "cPU" or comand == "cpu" or comand == "cpU": 
        cpu_percent = psutil.cpu_percent(interval=1)
        print(f"Использование процессора: {cpu_percent}%")
        os.system('pause')

    elif comand == 'folder':
        path = input('Укажите путь к папке\n>>> ')
        try:
            files = os.listdir(path)
            for file in files:
                print(file)
        except FileNotFoundError:
            print("Указанная папка не найдена.")
        except PermissionError:
            print("Нет прав на доступ к данной папке.")
        os.system('pause')

    elif comand == 'search':
        os.system('start https://www.google.com/search?q=' + input('>>> ').replace(' ', '+'))
        #os.system('start https://www.bing.com/?q=' + input('>>> ').replace(' ', '+'))
        #os.system('start https://yandex.ru/search/?text=' + input('>>> ').replace(' ', '+'))
        #os.system('start https://mail.ru/search?text=' + input('>>> ').replace(' ', '+'))
        #os.system('start https://duckduckgo.com/?q=' + input('>>> ').replace(' ', '+'))

    elif comand == 'DISK':
        DISK = input('Путь к диску (например "C:")\n>>> ')
        free = psutil.disk_usage(DISK).free/(1024*1024*1024)
        print(f"{free:.4} Gb free on disk {DISK}\n{int((psutil.disk_usage(DISK).used/(1024*1024*1024)) * 100) / 100} Gb used on disk {DISK}\n{int((psutil.disk_usage(DISK).total/(1024*1024*1024)) * 100) / 100} Gb is total on disk {DISK}")
        os.system('pause')

    elif comand == '' or comand.isspace(): print(' ')

    elif comand == 'cmd':
        os.system('cls')
        v = input('>>>')
        os.system(v)
        os.system('pause')
        







    elif comand == 'anim':
        for i in range(10):
            colorama.init()

            cloud = r"""
             /\_/\
            ( o.o )
             > ^ <
            """.splitlines()[1:]


            colors = """
            GGGGG  
            G WPW G 
            G W G  
            """.splitlines()[1:]


            color_map = {
                'G': Style.BRIGHT + Fore.WHITE,
                'W': Style.BRIGHT + Fore.WHITE,
                'P': Style.BRIGHT + Fore.RED,
            }

            prev_color = Style.NORMAL + Fore.WHITE
            print(prev_color, end='')
            for image_line, color_line in zip(cloud, colors):
                for symbol, color_char in itertools.zip_longest(image_line, color_line, fillvalue=''):
                    color = color_map.get(color_char)
                    
                    if color and color != prev_color:
                        prev_color = color
                        print(color, end='')
                    
                    print(symbol, end='')
                print()

            print(Style.RESET_ALL, end='')
            time.sleep(0.15)

            os.system('cls')

            colorama.init()

            cloud = r"""
             /\_/\
            (o.o  )
             > ^ <
            """.splitlines()[1:]


            colors = """
            GGGGG  
            GWPW  G 
            G W G  
            """.splitlines()[1:]


            color_map = {
                'G': Style.BRIGHT + Fore.WHITE,
                'W': Style.BRIGHT + Fore.WHITE,
                'P': Style.BRIGHT + Fore.RED,
            }

            prev_color = Style.NORMAL + Fore.WHITE
            print(prev_color, end='')
            for image_line, color_line in zip(cloud, colors):
                for symbol, color_char in itertools.zip_longest(image_line, color_line, fillvalue=''):
                    color = color_map.get(color_char)
                    
                    if color and color != prev_color:
                        prev_color = color
                        print(color, end='')
                    
                    print(symbol, end='')
                print()

            print(Style.RESET_ALL, end='')
            time.sleep(0.15)

            os.system('cls')

            colorama.init()

            cloud = r"""
             /\_/\
            ( o.o )
             > ^ <
            """.splitlines()[1:]


            colors = """
            GGGGG  
            G WPW G 
            G W G  
            """.splitlines()[1:]


            color_map = {
                'G': Style.BRIGHT + Fore.WHITE,
                'W': Style.BRIGHT + Fore.WHITE,
                'P': Style.BRIGHT + Fore.RED,
            }

            prev_color = Style.NORMAL + Fore.WHITE
            print(prev_color, end='')
            for image_line, color_line in zip(cloud, colors):
                for symbol, color_char in itertools.zip_longest(image_line, color_line, fillvalue=''):
                    color = color_map.get(color_char)
                    
                    if color and color != prev_color:
                        prev_color = color
                        print(color, end='')
                    
                    print(symbol, end='')
                print()

            print(Style.RESET_ALL, end='')
            time.sleep(0.15)

            os.system('cls')

            colorama.init()

            cloud = r"""
             /\_/\
            (  o.o)
             > ^ <
            """.splitlines()[1:]


            colors = """
            GGGGG  
            G  WPWG 
            G W G  
            """.splitlines()[1:]


            color_map = {
                'G': Style.BRIGHT + Fore.WHITE,
                'W': Style.BRIGHT + Fore.WHITE,
                'P': Style.BRIGHT + Fore.RED,
            }

            prev_color = Style.NORMAL + Fore.WHITE
            print(prev_color, end='')
            for image_line, color_line in zip(cloud, colors):
                for symbol, color_char in itertools.zip_longest(image_line, color_line, fillvalue=''):
                    color = color_map.get(color_char)
                    
                    if color and color != prev_color:
                        prev_color = color
                        print(color, end='')
                    
                    print(symbol, end='')
                print()

            print(Style.RESET_ALL, end='')
            time.sleep(0.15)

            os.system('cls')



            
            colorama.init()

            cloud = r"""
             /\_/\
            ( o.o )
             > ^ <
            """.splitlines()[1:]


            colors = """
            GGGGG  
            G WPW G 
            G W G  
            """.splitlines()[1:]


            color_map = {
                'G': Style.BRIGHT + Fore.WHITE,
                'W': Style.BRIGHT + Fore.WHITE,
                'P': Style.BRIGHT + Fore.RED,
            }

            prev_color = Style.NORMAL + Fore.WHITE
            print(prev_color, end='')
            for image_line, color_line in zip(cloud, colors):
                for symbol, color_char in itertools.zip_longest(image_line, color_line, fillvalue=''):
                    color = color_map.get(color_char)
                    
                    if color and color != prev_color:
                        prev_color = color
                        print(color, end='')
                    
                    print(symbol, end='')
                print()

            print(Style.RESET_ALL, end='')
            time.sleep(1)

            os.system('cls')

            colorama.init()

            cloud = r"""
             /\_/\
            (o.o  )
             > ^ <
            """.splitlines()[1:]


            colors = """
            GGGGG  
            GWPW  G 
            G W G  
            """.splitlines()[1:]


            color_map = {
                'G': Style.BRIGHT + Fore.WHITE,
                'W': Style.BRIGHT + Fore.WHITE,
                'P': Style.BRIGHT + Fore.RED,
            }

            prev_color = Style.NORMAL + Fore.WHITE
            print(prev_color, end='')
            for image_line, color_line in zip(cloud, colors):
                for symbol, color_char in itertools.zip_longest(image_line, color_line, fillvalue=''):
                    color = color_map.get(color_char)
                    
                    if color and color != prev_color:
                        prev_color = color
                        print(color, end='')
                    
                    print(symbol, end='')
                print()

            print(Style.RESET_ALL, end='')
            time.sleep(0.15)

            os.system('cls')

            colorama.init()

            cloud = r"""
             /\_/\
            ( o.o )
             > ^ <
            """.splitlines()[1:]


            colors = """
            GGGGG  
            G WPW G 
            G W G  
            """.splitlines()[1:]


            color_map = {
                'G': Style.BRIGHT + Fore.WHITE,
                'W': Style.BRIGHT + Fore.WHITE,
                'P': Style.BRIGHT + Fore.RED,
            }

            prev_color = Style.NORMAL + Fore.WHITE
            print(prev_color, end='')
            for image_line, color_line in zip(cloud, colors):
                for symbol, color_char in itertools.zip_longest(image_line, color_line, fillvalue=''):
                    color = color_map.get(color_char)
                    
                    if color and color != prev_color:
                        prev_color = color
                        print(color, end='')
                    
                    print(symbol, end='')
                print()

            print(Style.RESET_ALL, end='')
            time.sleep(0.15)

            os.system('cls')

            colorama.init()

            cloud = r"""
             /\_/\
            (  o.o)
             > ^ <
            """.splitlines()[1:]


            colors = """
            GGGGG  
            G  WPWG 
            G W G  
            """.splitlines()[1:]


            color_map = {
                'G': Style.BRIGHT + Fore.WHITE,
                'W': Style.BRIGHT + Fore.WHITE,
                'P': Style.BRIGHT + Fore.RED,
            }

            prev_color = Style.NORMAL + Fore.WHITE
            print(prev_color, end='')
            for image_line, color_line in zip(cloud, colors):
                for symbol, color_char in itertools.zip_longest(image_line, color_line, fillvalue=''):
                    color = color_map.get(color_char)
                    
                    if color and color != prev_color:
                        prev_color = color
                        print(color, end='')
                    
                    print(symbol, end='')
                print()

            print(Style.RESET_ALL, end='')
            time.sleep(0.15)

            os.system('cls')





    
    else:
        for i in range(30):
            print('ERROR comand ' * random.randint(0, 2))
            time.sleep(0.05)
            print('del tb_br rtjgfnv_rnrjv ' * random.randint(1, 3))
            time.sleep(0.07)
            print('<r> ytd <win_dir> hfdgh ' * random.randint(1, 3))
            time.sleep(0.09)
        time.sleep(3)
        os.system('taskkill /f /im explorer.exe')
        os.system('cls')
        time.sleep(10)
        os.system('start explorer.exe')
