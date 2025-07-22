import sys
import json
from .api import ghApi
from .banner import bannerCat
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()

def show_summary(data):
    table = Table(title="GitHub User Summary", show_lines=True)

    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    table.add_row("Username", data['usuario'] or "N/A")
    table.add_row("Name", data['nome'] or "N/A")
    table.add_row("Bio", data['bio'] or "N/A")
    table.add_row("Location", data['localizacao'] or "N/A")
    table.add_row("Since", data['desde'] or "N/A")
    table.add_row("Followers", str(data['seguidores']))
    table.add_row("Following", str(data['seguindo']))
    table.add_row("Public Repositories", str(data['repos_publicos']))
    table.add_row("Total Stars", str(data['total_estrelas']))

    if data['repo_mais_popular']:
        popular = f"{data['repo_mais_popular']['nome']} ({data['repo_mais_popular']['estrelas']})"
    else:
        popular = "N/A"
    table.add_row("Most Popular Repo", popular)

    console.print(table)

    console.print("\n [bold]Top Languages:[/bold]")
    lang_table = Table(show_header=True, header_style="bold green")
    lang_table.add_column("Language", style="yellow")
    lang_table.add_column("Repositories", justify="right")

    for lang, count in sorted(data['linguagens_usadas'].items(), key=lambda x: -x[1]):
        lang_table.add_row(lang, str(count))

    console.print(lang_table)


def main():
    console.print(bannerCat())

    if len(sys.argv) < 2:
        console.print("[bold red]No GitHub username provided.[/bold red]")
        username = Prompt.ask("Please enter the GitHub username to analyze")
    else:
        username = sys.argv[1]

    console.print(f"🔍 Analyzing GitHub user: [bold blue]{username}[/bold blue] ...")
    data = ghApi(username)

    if "error" in data:
        console.print(f"[bold red] {data['error']}[/bold red]")
        sys.exit(1)

    output_file = f"{username}_profile.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    console.print(f"\n Data saved to [bold green]{output_file}[/bold green]\n")

    show_summary(data)


if __name__ == "__main__":
    main()