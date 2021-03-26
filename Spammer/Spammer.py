import pyautogui as pag
from rich.console import Console
from rich.progress import Progress
import pyfiglet
from time import sleep

console = Console()

title = pyfiglet.figlet_format("SPAMMER", font="slant")
console.print(f"[yellow]{title}[/yellow]")
console.print('#'*14, style='red', end=' ')
console.print("Spam Your Message", style='yellow', end=' ')
console.print('#'*14, style='red')

console.print("\n[yellow]Enter text (separate with '>'): [/yellow]", end='')
text = input()
if text=='' or text==None:
    exit()
text = text.split('>')

console.print("\n[yellow]Enter delay: [/yellow]", end='')
delay = input()
if delay=='' or delay==None:
    delay = 0
else:
    try:
        delay = float(delay)
    except Exception:
        delay = 0

console.print("\n[yellow]Enter quantity: [/yellow]", end='')
quant = input()
if quant=='' or quant==None:
    quant = 1
else:
    try:
        quant = int(quant)
    except Exception:
        quant = 1

console.print()
for msg, index in zip(text, range(1, len(text)+1)):
    console.print(f"\t[[green]MESSAGE {index}[/green]] "+msg)
console.print("\t[[green]DELAY[/green]] "+str(delay)+' sec.')
console.print("\t[[green]QUANTITY[/green]] "+str(quant))
console.print("""\n[red]In 5 seconds it will start spamming messages,
open the window where you want them to be sent[/red]""")
input("\nPress any key to continue...")

list_msg = text*quant
advance_bar = 100/len(list_msg)

sleep(5)

console.clear()
console.print(f"[yellow]{title}[/yellow]")
console.print('#'*14, style='red', end=' ')
console.print("Spam Your Message", style='yellow', end=' ')
console.print('#'*14, style='red', end="\n\n")

try:
    flag = 0
    with Progress() as progress:
        task = progress.add_task("[green]Sending", total=100)

        while not progress.finished:
            pag.write(list_msg[flag])
            pag.press('enter')
            flag += 1
            sleep(delay)
            progress.update(task, advance=advance_bar)
except Exception as e:
    console.print("\n\t[[red]ERROR[/red]] "+e)
    console.print("\t[[green]INTERRUPTION[/green]] "+"None")
    console.print("\t[[red]STATUS[/red]] "+"not completed")
except KeyboardInterrupt:
    console.print("\n\t[[green]ERROR[/green]] "+"None")
    console.print("\t[[red]INTERRUPTION[/red]] "+e)
    console.print("\t[[yellow]STATUS[/yellow]] "+"partially completed")
else:
    console.print("\n\t[[green]ERROR[/green]] "+"None")
    console.print("\t[[green]INTERRUPTION[/green]] "+"None")
    console.print("\t[[green]STATUS[/green]] "+"complete")
    console.print("\n[red]♥[/red] with love by @_ste._bra__ [red]♥[/red]")

input()