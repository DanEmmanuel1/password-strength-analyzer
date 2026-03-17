import re
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from checker import check_breach
from generator import suggest_password
from reporter import save_report

console = Console()

COMMON_PASSWORDS = [
    "password", "123456", "password123", "admin", "letmein",
    "qwerty", "abc123", "monkey", "1234567", "dragon",
    "master", "sunshine", "princess", "welcome", "shadow"
]

def analyze_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 16:
        score += 25
        feedback.append("[green]✔ Great length (16+ characters)[/green]")
    elif len(password) >= 12:
        score += 15
        feedback.append("[yellow]⚠ Good length but 16+ is recommended[/yellow]")
    elif len(password) >= 8:
        score += 5
        feedback.append("[red]✘ Minimum length met but too short — use 12+ characters[/red]")
    else:
        feedback.append("[red]✘ Too short — must be at least 8 characters[/red]")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 15
        feedback.append("[green]✔ Contains uppercase letters[/green]")
    else:
        feedback.append("[red]✘ No uppercase letters — add at least one[/red]")

    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 15
        feedback.append("[green]✔ Contains lowercase letters[/green]")
    else:
        feedback.append("[red]✘ No lowercase letters — add at least one[/red]")

    # Number check
    if re.search(r'[0-9]', password):
        score += 15
        feedback.append("[green]✔ Contains numbers[/green]")
    else:
        feedback.append("[red]✘ No numbers — add at least one[/red]")

    # Special character check
    if re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password):
        score += 20
        feedback.append("[green]✔ Contains special characters[/green]")
    else:
        feedback.append("[red]✘ No special characters — add !@#$% etc[/red]")

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("[red]✘ This is one of the most common passwords — never use it![/red]")

    # Repeated characters check
    if re.search(r'(.)\1{2,}', password):
        score -= 10
        feedback.append("[yellow]⚠ Contains repeated characters (e.g. aaa) — avoid this[/yellow]")

    # Sequential characters check
    if re.search(r'(012|123|234|345|456|567|678|789|890|abc|bcd|cde|def)', password.lower()):
        score -= 10
        feedback.append("[yellow]⚠ Contains sequential characters (e.g. 123) — avoid this[/yellow]")

    score = max(0, min(score, 100))
    return score, feedback

def get_strength_label(score):
    if score >= 80:
        return "[bold green]STRONG[/bold green]"
    elif score >= 60:
        return "[bold yellow]MODERATE[/bold yellow]"
    elif score >= 40:
        return "[bold orange3]WEAK[/bold orange3]"
    else:
        return "[bold red]VERY WEAK[/bold red]"

def run():
    console.print(Panel.fit(
        "[bold cyan]Password Strength Analyzer[/bold cyan]\n"
        "[yellow]Version 1.0 — Free & Open Source[/yellow]\n"
        "[white]Checks strength, breaches & suggests better passwords[/white]",
        border_style="cyan"
    ))

    while True:
        console.print("\n[bold white]Options:[/bold white]")
        console.print("  [cyan]1[/cyan] — Analyze a password")
        console.print("  [cyan]2[/cyan] — Generate strong passwords")
        console.print("  [cyan]3[/cyan] — Exit")

        choice = input("\nChoose an option (1/2/3): ").strip()

        if choice == "1":
            password = input("Enter password to analyze: ").strip()

            if not password:
                console.print("[red]No password entered[/red]")
                continue

            console.print("\n[bold cyan]═══ ANALYSIS RESULTS ═══[/bold cyan]")

            score, feedback = analyze_password(password)
            strength = get_strength_label(score)
            breached = check_breach(password)

            console.print(f"\n[bold]Strength:[/bold] {strength}")
            console.print(f"[bold]Score:[/bold] {score}/100\n")

            console.print("[bold]Detailed Feedback:[/bold]")
            for item in feedback:
                console.print(f"  {item}")

            if score < 80:
                suggest_password()

            save_report(password, score, feedback, breached)

        elif choice == "2":
            suggest_password()

        elif choice == "3":
            console.print("\n[bold cyan]Goodbye! Stay secure. 🔐[/bold cyan]\n")
            break

        else:
            console.print("[red]Invalid option — choose 1, 2 or 3[/red]")

if __name__ == "__main__":
    run()
