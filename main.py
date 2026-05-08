import sys
from utile.display import print_banner, console
from module.phone import PhonyNode
from module.web import WebScanner
from module.mail import EmailOSINT
from module.pseudo import UsernameOSINT
from module.scan import NetworkScanner

def main():
    print_banner()
    console.print("\n[bold cyan]1.[/bold cyan] 📱 Téléphone")
    console.print("[bold cyan]2.[/bold cyan] 🌐 Web/IP")
    console.print("[bold cyan]3.[/bold cyan] 📧 Email")
    console.print("[bold cyan]4.[/bold cyan] 👤 Pseudo/Username")
    console.print("[bold orange1]5.[/bold orange1] 📡 Scan Réseau (Ports)")
    console.print("[bold red]0.[/bold red] Quitter")

    choice = console.input("\n[bold yellow]➤ Choix : [/bold yellow]")
    if choice == "0": sys.exit()

    target = console.input("[bold yellow]➤ Cible (IP/Domain/Email/etc) : [/bold yellow]").strip()

    if choice == "1":
        PhonyNode(target).run_scan()
    elif choice == "2":
        WebScanner(target).scan_infra()
    elif choice == "3":
        EmailOSINT(target).run_scan()
    elif choice == "4":
        UsernameOSINT(target).run_scan()
    elif choice == "5":
        NetworkScanner(target).run_scan()
    else:
        console.print("[bold red]Choix invalide[/bold red]")

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            console.print("\n[bold red]Arrêt du programme...[/bold red]")
            sys.exit()