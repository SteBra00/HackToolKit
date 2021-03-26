import os
import json
import pyfiglet
import socket
from multiprocessing.pool import ThreadPool
from rich.console import Console
from rich.progress import Progress
from rich.table import Table

ports = {}
list_ports_opened = []
target = ""


def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)
    conn_status = sock.connect_ex((target, port))
    if conn_status == 0:
        list_ports_opened.append(port)
    sock.close()


with open("source/common_ports.json", 'r') as file:
    for k, e in json.load(file).items():
        ports[int(k)] = e


console = Console()

title = pyfiglet.figlet_format("P-SCAN", font="slant")
console.print(f"[blue]{title}[/blue]")
console.print('#'*10, style='yellow', end=' ')
console.print("Port Scanner TCP/IP", style='blue', end=' ')
console.print('#'*10, style='yellow')


console.print("\nEnter Target: ", style="blue", end="")
target = input()
try:
    target = socket.gethostbyname(target)
except socket.gaierror:
    exit()

worker = os.cpu_count()
console.print("\n\t[[green]TARGET[/green]] "+target)
console.print("\t[[green]WORKER[/green]] "+str(worker))
input("\nPress any key to continue...")

console.clear()
title = pyfiglet.figlet_format("P-SCAN", font="slant")
console.print(f"[blue]{title}[/blue]")
console.print('#'*10, style='yellow', end=' ')
console.print("Port Scanner TCP/IP", style='blue', end=' ')
console.print('#'*10, style='yellow', end='\n\n')

try:
    with Progress() as progress:
        advance_bar = 100/len(ports.keys())
        task = progress.add_task("[green]Scanning", total=100)
        with ThreadPool(worker) as pool:
            for loop_index, _ in enumerate(pool.imap(scan_port, ports.keys()), 1):
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
    console.print("\t[[green]STATUS[/green]] "+"complete\n")

if len(list_ports_opened)>0:
    table = Table(show_header=True, header_style="red")
    table.add_column("PORT", style="blue")
    table.add_column("STATE", style="blue", justify="center")
    table.add_column("SERVICE", style="blue")
    for port in list_ports_opened:
        table.add_row(str(port), "OPEN", ports[port])
    console.print(table)
        

console.print("\n[red]♥[/red] with love by @_ste._bra__ [red]♥[/red]")
input()