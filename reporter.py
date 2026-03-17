from datetime import datetime
from rich.console import Console

console = Console()

REPORT_FILE = "password_report.txt"

def save_report(password, score, feedback, breached):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    masked = password[:2] + "*" * (len(password) - 2)

    lines = []
    lines.append("=" * 50)
    lines.append(f"Date:      {now}")
    lines.append(f"Password:  {masked}")
    lines.append(f"Score:     {score}/100")
    lines.append(f"Breached:  {'YES - DANGER' if breached else 'No'}")
    lines.append("Feedback:")

    for item in feedback:
        clean = item
        for tag in ["[red]","[/red]","[green]","[/green]",
                    "[yellow]","[/yellow]","[bold]","[/bold]",
                    "[orange3]","[/orange3]"]:
            clean = clean.replace(tag, "")
        # Remove special symbols
        clean = clean.replace("\u2718", "FAIL")
        clean = clean.replace("\u2714", "PASS")
        clean = clean.replace("\u26a0", "WARN")
        clean = clean.replace("\u2713", "PASS")
        lines.append(f"  - {clean}")

    lines.append("=" * 50)
    lines.append("")

    try:
        with open(REPORT_FILE, "a", encoding="ascii", errors="replace") as f:
            f.write("\n".join(lines) + "\n")
        console.print(f"[green]✔ Report saved to {REPORT_FILE}[/green]")
    except Exception as e:
        console.print(f"[red]✘ Could not save report: {e}[/red]")