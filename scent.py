from rich.console import Console
import questionary
import pyfiglet
from scans.icmp_sweep import icmp_sweep
from scans.tcp_scan import tcp_scan
from scans.udp_scan import udp_scan

# Initialize the console for rich output
console = Console()

def banner():
    ascii_art = pyfiglet.figlet_format("Scent", font = "isometric1")
    print(ascii_art)

    print("----------------------------------------------------------------------")
    print("Welcome to Scent — Follow the Trail, Uncover the Network")
    print("----------------------------------------------------------------------\n")

def menu():
    banner()

    choice = questionary.select(
        "Choose an option:",
        choices=[
            "ICMP Sweep",
            "TCP Scan",
            "UDP Scan",
            "Exit",
        ],
    ).ask()

    if choice == "ICMP Sweep":
        ip_range = questionary.text("Enter network range (e.g., 192.168.1.0/24):").ask()
        icmp_sweep(ip_range)
    elif choice == "TCP Scan":
        target_ip = questionary.text("Enter the target IP address:").ask()
        port_range = questionary.text("Enter port range (default: 1-1024):").ask()
        if port_range == "":
            port_range = "1-1024"
        console.print("[green]Scanning network...[/green]")
        tcp_scan(target_ip, port_range)
    elif choice == "UDP Scan":
        target_ip = questionary.text("Enter the target IP address:").ask()
        port_range = questionary.text("Enter port range (default: 1-1024):").ask()
        if port_range == "":
            port_range = "1-1024"
        console.print("[green]Scanning network...[/green]")
        udp_scan(target_ip, port_range)
    else:
        console.print("[red]Exiting...[/red]")
        exit()

if __name__ == "__main__":
    menu()