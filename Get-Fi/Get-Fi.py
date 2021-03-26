import os
import sys
from rich.console import Console
import pyfiglet
from time import sleep


list_ssid = []
console = Console()

title = pyfiglet.figlet_format("Get-Fi", font="slant")
console.print(f"[red]{title}[/red]")
console.print('#'*5, style='color(5)', end=' ')
console.print("Get Data of All Wi-Fi", style='red', end=' ')
console.print('#'*5, style='color(5)')

def run():
    sleep(0.5)
    if sys.platform!='win32':
        console.print("\n\t[[red]OS win32[/red]] "+"error")
        return False
    else:
        console.print("\n\t[[green]OS win32[/green]] "+"ok")
    
    sleep(0.5)
    try:
        os.system('netsh wlan show profiles > text.txt')
    except Exception:
        console.print("\t[[red]VIEW SSID[/red]] "+"error")
        return False
    else:
        console.print("\t[[green]VIEW SSID[/green]] "+"ok")
    
    sleep(0.5)
    try:
        with open('text.txt', 'r') as f:
            text = f.readlines()
        for line in text:
            if (':' in line) and line.startswith("    "):
                list_ssid.append(line.split(": ")[-1][:-1])
    except Exception:
        console.print("\t[[red]GET DATA[/red]] "+"error")
        return False
    else:
        console.print("\t[[green]GET DATA[/green]] "+"ok")
    
    sleep(0.5)
    try:
        os.remove('text.txt')
        if not os.path.exists('source'):
            os.system('mkdir source')
        for ssid in list_ssid:
            os.system(f'netsh wlan show profile "{ssid}" key=clear > "source\\{ssid}.txt"')
    except Exception:
        console.print("\t[[red]SAVE DATA[/red]] "+"error")
        return False
    else:
        console.print("\t[[green]SAVE DATA[/green]] "+"ok")
        return True


if run():
    console.print("\n\n[red]♥[/red] with love by @_ste._bra__ [red]♥[/red]")

input()
