from scapy.all import ICMP, IP, sr
from rich.console import Console

console = Console()

def icmp_sweep(ip_range):
    console.print(f"[*] Scanning {ip_range} for active hosts...", style="cyan")

    # Send ICMP Echo Request (ping) packets
    ans, _ = sr(IP(dst=ip_range)/ICMP(), timeout=2, verbose=False)

    # Process responses
    active_hosts = [recv_pkt[IP].src for send_pkt, recv_pkt in ans]

    if active_hosts:
        console.print("[+] Active Hosts:", style="green")
        for host in active_hosts:
            console.print(f"    - {host}", style="bold green")
    else:
        console.print("[-] No active hosts found.", style="red")