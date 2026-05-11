import sys
import os
from utile.display import print_banner, console
from module.password import PasswordAnalyzer
from module.sniffeur import NetworkSniffer
from module.phone import PhonyNode
from module.web import WebScanner
from module.mail import EmailOSINT
from module.pseudo import UsernameOSINT
from module.scan import NetworkScanner
from module.info import SystemDevis
from module.profileur import Profileur 
from module.danger import URLAnalyzer
from module.meta import MetadataExtractor
from module.ia import IADetector

def main():
    print_banner()
    console.print("\n[bold cyan]1.[/bold cyan] 📱 Téléphone")
    console.print("[bold cyan]2.[/bold cyan] 🌐 Web/IP")
    console.print("[bold cyan]3.[/bold cyan] 📧 Email")
    console.print("[bold cyan]4.[/bold cyan] 👤 Pseudo/Username")
    console.print("[bold cyan]5.[/bold cyan] 📡 Scan de Ports")
    console.print("[bold cyan]6.[/bold cyan] 🔍 Sniffeur Réseau")
    console.print("[bold red]7.[/bold red] 🔑 Testeur Mot de Passe")
    console.print("[bold red]8.[/bold red] 📋 Devis Système (Hardware)")
    console.print("[bold magenta]9.[/bold magenta] 🕵️  Profilage (Nom/Prénom)")
    console.print("[bold green]10.[/bold green] 🛡️  Vérifier URL (VirusTotal)")
    console.print("[bold green]11.[/bold green] 📂 Extraire Métadonnées (Image/Doc)")
    console.print("[bold green]12.[/bold green] 🤖 Détecteur de texte IA")
    
    console.print("[bold black]0.[/bold black] Quitter")

    choice = console.input("\n[bold yellow]➤ Choix : [/bold yellow]")
    if choice == "0": sys.exit()

    # --- Gestion des entrées utilisateur selon le module ---
    target = ""
    
    # Choix nécessitant une cible classique (IP, URL, Email, Tel)
    if choice in ["1", "2", "3", "4", "5", "6", "10"]:
        target = console.input("[bold yellow]➤ Cible : [/bold yellow]").strip()

    # Choix nécessitant un chemin de fichier
    elif choice in ["11", "12"]:
        target = console.input("[bold yellow]➤ Chemin du fichier : [/bold yellow]").strip()

    # --- Exécution des modules ---
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
    elif choice == "6":
        NetworkSniffer(target).run_scan()
    elif choice == "7":
        PasswordAnalyzer().run_scan()
    elif choice == "8":
        SystemDevis().run_scan()
    
    elif choice == "9":
        nom_input = console.input("[bold yellow]➤ NOM : [/bold yellow]").strip()
        prenom_input = console.input("[bold yellow]➤ PRÉNOM : [/bold yellow]").strip()
        age_input = console.input("[bold yellow]➤ ÂGE (Optionnel) : [/bold yellow]").strip()
        
        p = Profileur(nom=str(nom_input), prenom=str(prenom_input), age=age_input if age_input else None)
        console.print("[bold blue][*] Recherche en cours... Patientez...[/bold blue]")
        p.executer_recherche_complete() 
        p.afficher_resultats() 

    # Intégration de tes nouveaux outils
    elif choice == "10":
        URLAnalyzer(target).run_scan()
    elif choice == "11":
        MetadataExtractor(target).run_scan()
    elif choice == "12":
        IADetector(target).run_scan()

    else:
        console.print("[bold red]Choix invalide[/bold red]")

if __name__ == "__main__":
    while True:
        try:
            main()
            console.input("\n[bold white]Appuyez sur Entrée pour revenir au menu...[/bold white]")
        except KeyboardInterrupt:
            console.print("\n[bold red]Arrêt du programme...[/bold red]")
            sys.exit()
        except Exception as e:
            console.print(f"\n[bold red]Erreur inattendue : {e}[/bold red]")