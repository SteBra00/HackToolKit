import os
from rich.console import Console
import pyfiglet

NAME = 'name'
PATH = 'path'
FILENAME = 'index.py'
_file_ = __file__.replace('\\', '/')
ROOT = _file_.rsplit('/', 1)[0]

console = Console()
console.clear()

title = pyfiglet.figlet_format(" HTK ", font="slant")
console.print(f"[green]{title}[/green]")
console.print('#'*5, style='color(5)', end=' ')
console.print("Hack Tool Kit", style='green', end=' ')
console.print('#'*5, style='color(5)', end='\n\n')

tools = []
for elem in os.listdir():
    if os.path.isdir(elem):
        list_sub_dir = os.listdir(elem)
        if FILENAME in list_sub_dir:
            tools.append({NAME:elem, PATH:elem+'/'+FILENAME})

if len(tools)>0:
    for i in range(len(tools)):
        console.print(f"\t{i}_ {tools[i][NAME]}", style='color(5)')
else:
    console.print(f"\t0 tool in this directory", style='color(5)')
    input()
    exit()

try:
    console.print('\nNumber:', style='color(5)', end=' ')
    index = int(input())
except ValueError:
    console.print(f"\t[ValueError]", style='red')

try:
    os.system(f"python3 {tools[index][PATH]}")
except Exception as e:
    print(e)
    input()