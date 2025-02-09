from rich.console import Console
import questionary
import pyfiglet
from scans.icmp_sweep import icmp_sweep

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
            "IPv6",
            "ICMP Sweep",
            "SYN Scan",
            "UDP Scan",
            "Settings",
            "Exit",
        ],
    ).ask()

    if choice == "SYN Scan":
        console.print("[green]Scanning network...[/green]")
        # Call network scan function
    elif choice == "ICMP Sweep":
        ip_range = questionary.text("Enter network range (e.g., 192.168.1.0/24):").ask()
        icmp_sweep(ip_range)
    elif choice == "Settings":
        console.print("[blue]Opening settings...[/blue]")
        # Add settings logic
    else:
        console.print("[red]Exiting...[/red]")
        exit()

if __name__ == "__main__":
    menu()