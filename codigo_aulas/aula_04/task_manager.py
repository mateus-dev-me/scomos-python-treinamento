import os
import time
import json
from typing import List
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

# Instância do console do Rich
console = Console()

# Arquivo para armazenar as tarefas
TASKS_FILE = "tasks.json"

# Lista de tarefas
tasks: List[str] = []

def load_tasks() -> None:
    """Carrega as tarefas do arquivo JSON."""
    global tasks
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r", encoding="utf-8") as file:
                tasks = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            tasks = []

def save_tasks() -> None:
    """Salva as tarefas no arquivo JSON."""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def add_task(task: str) -> None:
    """Adiciona uma tarefa à lista e salva."""
    tasks.append(task)
    save_tasks()
    console.print(f"[green]✔ Tarefa '{task}' adicionada com sucesso![/]")

def list_tasks() -> None:
    """Lista todas as tarefas pendentes."""
    if not tasks:
        console.print("[yellow]⚠ Nenhuma tarefa pendente.[/]")
        return
    
    table = Table(title=f"📌 Tarefas Pendentes ({len(tasks)})", show_header=True, header_style="bold magenta")
    table.add_column("#", justify="right", style="cyan", no_wrap=True)
    table.add_column("Tarefa", style="white")

    for i, task in enumerate(tasks, 1):
        table.add_row(str(i), task)

    console.print(table)

def remove_task(index: int) -> None:
    """Remove uma tarefa pelo índice informado e salva."""
    try:
        task = tasks.pop(index - 1)
        save_tasks()
        console.print(f"[red]🗑️ Tarefa '{task}' removida.[/]")
    except IndexError:
        console.print("[bold red]❌ Erro:[/] Índice inválido. Escolha um número da lista.")

def main() -> None:
    """Loop principal para interação com o usuário."""
    load_tasks()  # Carrega as tarefas ao iniciar

    while True:
        console.print("\n[bold blue]📌 Menu:[/]")
        console.print("[cyan]1.[/] Adicionar tarefa")
        console.print("[cyan]2.[/] Listar tarefas")
        console.print("[cyan]3.[/] Remover tarefa")
        console.print("[cyan]4.[/] Sair")

        opcao = Prompt.ask("\nEscolha uma opção", choices=["1", "2", "3", "4"], default="1")

        if opcao == "1":
            tarefa = Prompt.ask("📝 Digite a tarefa")
            add_task(tarefa)
        elif opcao == "2":
            list_tasks()
        elif opcao == "3":
            if not tasks:
                console.print("[yellow]⚠ Nenhuma tarefa para remover.[/]")
                continue
            list_tasks()
            try:
                indice = int(Prompt.ask("🗑️ Digite o número da tarefa para remover"))
                remove_task(indice)
            except ValueError:
                console.print("[bold red]❌ Erro:[/] Digite um número válido.")
        elif opcao == "4":
            console.print("[bold green]👋 Saindo... Até logo![/]")
            time.sleep(0.5)
            os.system('clear' if os.name == 'posix' else 'cls')
            break

if __name__ == "__main__":
    main()

