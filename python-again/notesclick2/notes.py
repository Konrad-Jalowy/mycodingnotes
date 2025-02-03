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
    """📝 Menedżer Notatek w Terminalu"""
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
    filtered_notes = [note for note in notes if note["id"] != note_id]

    if len(filtered_notes) == len(notes):
        click.echo(click.style(f"⚠️ Notatka {note_id} nie istnieje!", fg="red"))
        return

    save_notes(filtered_notes)
    click.echo(click.style(f"🗑️ Notatka {note_id} została usunięta!", fg="red"))

# 🔹 Komenda: Edycja notatki
@click.command()
@click.argument("note_id", type=int)
@click.argument("new_content")
def edit(note_id, new_content):
    """Edytuje istniejącą notatkę"""
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["content"] = new_content
            save_notes(notes)
            click.echo(click.style(f"✏️ Notatka {note_id} została zaktualizowana!", fg="blue"))
            return

    click.echo(click.style(f"⚠️ Notatka {note_id} nie istnieje!", fg="red"))

# 🔹 Komenda: Filtrowanie notatek po tytule
@click.command()
@click.argument("keyword")
def search(keyword):
    """Wyszukuje notatki zawierające podane słowo w tytule"""
    notes = load_notes()
    filtered_notes = [note for note in notes if keyword.lower() in note["title"].lower()]

    if not filtered_notes:
        click.echo(click.style(f"🔍 Brak notatek zawierających '{keyword}' w tytule.", fg="yellow"))
        return

    click.echo(click.style(f"\n🔍 Znalezione notatki dla '{keyword}':\n", fg="cyan", bold=True))
    for note in filtered_notes:
        click.echo(click.style(f"{note['id']}. {note['title']} - {note['content']}", fg="white"))

# 🔹 Komenda: Eksportowanie notatek do pliku TXT
@click.command()
@click.argument("filename", default="notes_export.txt")
def export(filename):
    """Eksportuje notatki do pliku tekstowego"""
    notes = load_notes()
    if not notes:
        click.echo(click.style("📭 Brak notatek do eksportu!", fg="yellow"))
        return

    with open(filename, "w", encoding="utf-8") as file:
        file.write("📌 Lista notatek:\n\n")
        for note in notes:
            file.write(f"{note['id']}. {note['title']} - {note['content']}\n")

    click.echo(click.style(f"📄 Notatki zostały zapisane w '{filename}'!", fg="green"))

# 🔹 Dodajemy komendy do CLI
cli.add_command(add)
cli.add_command(list, name="list")
cli.add_command(delete)
cli.add_command(edit)
cli.add_command(search)
cli.add_command(export)

if __name__ == "__main__":
    cli()
