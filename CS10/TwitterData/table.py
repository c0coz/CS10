from rich.console import Console
from rich.table import Column, Table
from main import *
console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Date", style="dim", width=12)
table.add_column("Author")
table.add_column("Text", justify="right")
table.add_row(y[0]["created_at"],y[0]["user"]["name"],y[0]["text"])
table.add_row(y[1]["created_at"],y[1]["user"]["name"],y[1]["text"])
table.add_row(y[2]["created_at"],y[2]["user"]["name"],y[2]["text"])
table.add_row(y[3]["created_at"],y[3]["user"]["name"],y[3]["text"])
table.add_row(y[4]["created_at"],y[4]["user"]["name"],y[4]["text"])

console.print(table)
