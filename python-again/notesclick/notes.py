import click
import json
import os

NOTES_FILE = "notes_data.json"

# 🔹 Funkcja pomocnicza – ładowanie notatek
def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

# 🔹 Funkcja pomocnicza – zapisywanie notatek
def save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4, ensure_ascii=False)

@click.group()
def cli():
    """Menedżer Notatek w Terminalu"""
    pass

# 🔹 Komenda: Dodawanie notatki
@click.command()
@click.argument("title")
@click.argument("content")
def add(title, content):
    """Dodaje nową notatkę"""
    notes = load_notes()
    notes.append({"id": len(notes) + 1, "title": title, "content": content})
    save_notes(notes)
    click.echo(click.style(f"✅ Notatka '{title}' została dodana!", fg="green"))

# 🔹 Komenda: Listowanie notatek
@click.command()
def list():
    """Wyświetla listę wszystkich notatek"""
    notes = load_notes()
    if not notes:
        click.echo(click.style("📭 Brak notatek!", fg="yellow"))
        return

    click.echo(click.style("\n📌 Lista notatek:\n", fg="cyan", bold=True))
    for note in notes:
        click.echo(click.style(f"{note['id']}. {note['title']} - {note['content']}", fg="white"))

# 🔹 Komenda: Usuwanie notatki
@click.command()
@click.argument("note_id", type=int)
def delete(note_id):
    """Usuwa notatkę po ID"""
    notes = load_notes()
    notes = [note for note in notes if note["id"] != note_id]

    save_notes(notes)
    click.echo(click.style(f"🗑️ Notatka {note_id} została usunięta!", fg="red"))

# 🔹 Dodajemy komendy do CLI
cli.add_command(add)
cli.add_command(list, name="list")
cli.add_command(delete)

if __name__ == "__main__":
    cli()
