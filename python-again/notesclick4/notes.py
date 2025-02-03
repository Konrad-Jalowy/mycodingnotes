import click
import json
import os
from datetime import datetime, timedelta
from collections import Counter

NOTES_FILE = "notes_data.json"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


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


# 🔹 Komenda: Dodawanie notatki z kategorią, datą i przypomnieniem
@click.command()
@click.argument("title")
@click.argument("content")
@click.option("--category", default="default", help="Kategoria notatki")
@click.option("--reminder", default=None, help="Data przypomnienia (YYYY-MM-DD HH:MM:SS)")
def add(title, content, category, reminder):
    """Dodaje nową notatkę z kategorią i przypomnieniem"""
    notes = load_notes()

    new_note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "category": category,
        "created_at": datetime.now().strftime(DATE_FORMAT),
        "reminder_at": reminder if reminder else None
    }
    notes.append(new_note)
    save_notes(notes)

    click.echo(click.style(f"✅ Notatka '{title}' została dodana!", fg="green"))
    if reminder:
        click.echo(click.style(f"⏰ Przypomnienie ustawione na {reminder}", fg="blue"))


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
        reminder_text = f"⏰ {note['reminder_at']}" if note["reminder_at"] else "🔕 Brak przypomnienia"
        click.echo(click.style(
            f"{note['id']}. [{note['category'].upper()}] {note['title']} - {note['content']} (Dodano: {note['created_at']}) {reminder_text}",
            fg="white"
        ))


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


# 🔹 Komenda: Filtrowanie notatek po kategorii
@click.command()
@click.argument("category")
def filter_by_category(category):
    """Wyświetla notatki według kategorii"""
    notes = load_notes()
    filtered_notes = [note for note in notes if note["category"].lower() == category.lower()]

    if not filtered_notes:
        click.echo(click.style(f"🔍 Brak notatek w kategorii '{category}'.", fg="yellow"))
        return

    click.echo(click.style(f"\n📂 Notatki w kategorii '{category}':\n", fg="cyan", bold=True))
    for note in filtered_notes:
        click.echo(click.style(
            f"{note['id']}. {note['title']} - {note['content']} (Dodano: {note['created_at']})",
            fg="white"
        ))


# 🔹 Komenda: Statystyki notatek
@click.command()
def stats():
    """Wyświetla statystyki notatek"""
    notes = load_notes()
    if not notes:
        click.echo(click.style("📭 Brak notatek!", fg="yellow"))
        return

    total_notes = len(notes)
    categories = Counter(note["category"] for note in notes)

    click.echo(click.style("\n📊 Statystyki notatek:\n", fg="cyan", bold=True))
    click.echo(click.style(f"📋 Łączna liczba notatek: {total_notes}", fg="green"))
    click.echo(click.style("\n📂 Podział na kategorie:", fg="magenta", bold=True))

    for category, count in categories.items():
        click.echo(click.style(f"  - {category}: {count} notatek", fg="white"))


# 🔹 Komenda: Wyświetlanie przypomnień
@click.command()
@click.option("--today", is_flag=True, help="Pokaż tylko przypomnienia na dzisiaj")
def reminders(today):
    """Wyświetla nadchodzące przypomnienia"""
    notes = load_notes()
    now = datetime.now()

    if today:
        filtered_notes = [
            note for note in notes if note["reminder_at"] and
                                      datetime.strptime(note["reminder_at"], DATE_FORMAT).date() == now.date()
        ]
        title = "📅 Przypomnienia na dziś:"
    else:
        filtered_notes = [note for note in notes if note["reminder_at"]]
        title = "⏳ Nadchodzące przypomnienia:"

    if not filtered_notes:
        click.echo(click.style(f"🔕 Brak przypomnień!", fg="yellow"))
        return

    click.echo(click.style(f"\n{title}\n", fg="cyan", bold=True))
    for note in filtered_notes:
        reminder_time = datetime.strptime(note["reminder_at"], DATE_FORMAT)
        time_left = reminder_time - now
        click.echo(click.style(
            f"{note['id']}. {note['title']} - {note['content']} (Przypomnienie: {note['reminder_at']}, za {time_left})",
            fg="white"
        ))


# 🔹 Dodajemy komendy do CLI
cli.add_command(add)
cli.add_command(list, name="list")
cli.add_command(delete)
cli.add_command(filter_by_category, name="filter")
cli.add_command(stats)
cli.add_command(reminders)

if __name__ == "__main__":
    cli()
