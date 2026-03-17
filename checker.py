import hashlib
import requests
from rich.console import Console

console = Console()

def check_breach(password):
    console.print("\n[bold]Breach Check:[/bold]")
    try:
        sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
        prefix = sha1[:5]
        suffix = sha1[5:]

        response = requests.get(
            f"https://api.pwnedpasswords.com/range/{prefix}",
            timeout=5
        )

        if response.status_code == 200:
            hashes = response.text.splitlines()
            for h in hashes:
                parts = h.split(":")
                if parts[0] == suffix:
                    count = int(parts[1])
                    console.print(f"[red]✘ This password appeared in {count:,} data breaches — NEVER use it![/red]")
                    return True
            console.print("[green]✔ This password has not been found in any known data breaches[/green]")
            return False
        else:
            console.print("[yellow]⚠ Could not connect to breach database[/yellow]")
            return False

    except Exception as e:
        console.print(f"[yellow]⚠ Breach check failed: {e}[/yellow]")
        return False