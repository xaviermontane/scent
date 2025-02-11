from scapy.all import IP, TCP, sr1
from rich.console import Console

console = Console()

def tcp_scan(target_ip, port_range):
    console.print(f"[*] Scanning {target_ip} for open TCP ports...", style="cyan")

    # Parse port range
    start_port, end_port = map(int, port_range.split('-'))
    port_range = range(start_port, end_port + 1)

    for port in port_range:
        # Create a TCP SYN packet
        packet = IP(dst=target_ip)/TCP(dport=port, flags="S")

        # Send packet and wait for response
        response = sr1(packet, timeout=1, verbose=False)

        # Analyze response
        if response:
            if response.haslayer(TCP):
                if response[TCP].flags == 0x12:  # SYN-ACK (Port is open)
                    console.print(f"[green][+] {port}/TCP is open![/green]")
                elif response[TCP].flags == 0x14:  # RST-ACK (Port is closed)
                    console.print(f"[red][-] {port}/TCP is closed.[/red]")
            else:
                console.print(f"[yellow][?] {port}/TCP is filtered or unresponsive.[/yellow]")
        else:
            console.print(f"[yellow][?] {port}/TCP is filtered (no response).[/yellow]")