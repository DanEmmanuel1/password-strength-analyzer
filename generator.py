import random
import string
from rich.console import Console

console = Console()

def generate_strong_password(length=16):
    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        "!@#$%^&*()_+-=[]{}|;:,.<>?"
    )

    while True:
        password = ''.join(random.choices(characters, k=length))
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)

        if has_upper and has_lower and has_digit and has_special:
            return password

def suggest_password():
    console.print("\n[bold]Suggested Strong Passwords:[/bold]")
    for i in range(3):
        pwd = generate_strong_password()
        console.print(f"[green]  {i+1}. {pwd}[/green]")