from scapy.all import IP, UDP, sr1
from rich.console import Console

console = Console()

def udp_scan(target_ip, port_range):
    console.print(f"[*] Scanning {target_ip} for open UDP ports...", style="cyan")

    # Parse port range
    start_port, end_port = map(int, port_range.split('-'))
    port_range = range(start_port, end_port + 1)

    for port in port_range:
        # Create a UDP packet
        packet = IP(dst=target_ip)/UDP(dport=port)

        # Send packet and wait for response
        response = sr1(packet, timeout=1, verbose=False)

        # Analyze response
        if response:
            if response.haslayer(UDP):
                console.print(f"[green][+] {port}/UDP is open![/green]")
            else:
                console.print(f"[yellow][?] {port}/UDP is filtered or unresponsive.[/yellow]")
        else:
            console.print(f"[yellow][?] {port}/UDP is filtered (no response).[/yellow]")