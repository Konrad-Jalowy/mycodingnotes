using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Xml.Linq;
using Newtonsoft.Json;

class Program
{
    class Person
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public int Age { get; set; }
    }

    static void Main()
    {
        string jsonFilePath = "dane.json";
        var people = ReadFromJson(jsonFilePath);
        Console.WriteLine("Dane wczytane.");

        Console.WriteLine("Dostępne komendy: list, show <id>, add, edit <id>, remove <id>, savecsv <filename>, savexml <filename>, exit, help");

        while (true)
        {
            Console.Write("Komenda: ");
            string input = Console.ReadLine()?.Trim();
            if (string.IsNullOrWhiteSpace(input)) continue;

            var parts = input.Split(' ', 2);
            string command = parts[0].ToLower();
            string argument = parts.Length > 1 ? parts[1] : null;

            switch (command)
            {
                case "list":
                    DisplayAll(people);
                    break;
                case "show":
                    if (int.TryParse(argument, out int showId))
                        DisplaySingle(people, showId);
                    else
                        Console.WriteLine("Podaj poprawne ID.");
                    break;
                case "add":
                    AddPerson(people);
                    break;
                case "edit":
                    if (int.TryParse(argument, out int editId))
                        EditPerson(people, editId);
                    else
                        Console.WriteLine("Podaj poprawne ID.");
                    break;
                case "remove":
                    if (int.TryParse(argument, out int removeId))
                        RemovePerson(people, removeId);
                    else
                        Console.WriteLine("Podaj poprawne ID.");
                    break;
                case "savecsv":
                    if (!string.IsNullOrWhiteSpace(argument))
                    {
                        SaveToCsv(argument, people);
                        Console.WriteLine($"Dane zapisane do {argument}.");
                    }
                    else
                        Console.WriteLine("Podaj nazwę pliku CSV.");
                    break;
                case "savexml":
                    if (!string.IsNullOrWhiteSpace(argument))
                    {
                        SaveToXml(argument, people);
                        Console.WriteLine($"Dane zapisane do {argument}.");
                    }
                    else
                        Console.WriteLine("Podaj nazwę pliku XML.");
                    break;
                case "exit":
                    SaveToJson(jsonFilePath, people);
                    return;
                case "help":
                    Console.WriteLine("Dostępne komendy: list, show <id>, add, edit <id>, remove <id>, savecsv <filename>, savexml <filename>, exit, help");
                    break;
                default:
                    Console.WriteLine("Nieznana komenda. Wpisz 'help', aby zobaczyć listę dostępnych komend.");
                    break;
            }
        }
    }

    static void DisplayAll(List<Person> people)
    {
        foreach (var p in people)
            Console.WriteLine($"ID: {p.Id}, Imię: {p.Name}, Wiek: {p.Age}");
    }

    static void DisplaySingle(List<Person> people, int id)
    {
        var person = people.FirstOrDefault(p => p.Id == id);
        if (person != null)
            Console.WriteLine($"ID: {person.Id}, Imię: {person.Name}, Wiek: {person.Age}");
        else
            Console.WriteLine("Nie znaleziono osoby o podanym ID.");
    }

    static void AddPerson(List<Person> people)
    {
        Console.Write("Podaj ID: ");
        int id = int.Parse(Console.ReadLine());
        Console.Write("Podaj imię: ");
        string name = Console.ReadLine();
        Console.Write("Podaj wiek: ");
        int age = int.Parse(Console.ReadLine());
        people.Add(new Person { Id = id, Name = name, Age = age });
    }

    static void EditPerson(List<Person> people, int id)
    {
        var person = people.FirstOrDefault(p => p.Id == id);
        if (person != null)
        {
            Console.Write($"Nowe imię [{person.Name}]: ");
            string newName = Console.ReadLine();
            if (!string.IsNullOrWhiteSpace(newName))
                person.Name = newName;
            Console.Write($"Nowy wiek [{person.Age}]: ");
            string newAge = Console.ReadLine();
            if (!string.IsNullOrWhiteSpace(newAge))
                person.Age = int.Parse(newAge);
            Console.WriteLine("Dane osoby zaktualizowane.");
        }
        else
            Console.WriteLine("Nie znaleziono osoby o podanym ID.");
    }

    static void RemovePerson(List<Person> people, int id)
    {
        var person = people.FirstOrDefault(p => p.Id == id);
        if (person != null)
        {
            people.Remove(person);
            Console.WriteLine("Osoba usunięta.");
        }
        else
            Console.WriteLine("Nie znaleziono osoby o podanym ID.");
    }

    static void SaveToCsv(string filePath, List<Person> people)
    {
        File.WriteAllLines(filePath, people.Select(p => $"{p.Id},{p.Name},{p.Age}"));
    }

    static void SaveToXml(string filePath, List<Person> people)
    {
        XDocument xmlDoc = new XDocument(
            new XElement("People",
                people.Select(p => new XElement("Person",
                    new XElement("Id", p.Id),
                    new XElement("Name", p.Name),
                    new XElement("Age", p.Age)
                ))
            )
        );
        xmlDoc.Save(filePath);
    }

    static void SaveToJson(string filePath, List<Person> people)
    {
        string json = JsonConvert.SerializeObject(people, Formatting.Indented);
        File.WriteAllText(filePath, json);
    }

    static List<Person> ReadFromJson(string filePath)
    {
        if (!File.Exists(filePath)) return new List<Person>();
        string json = File.ReadAllText(filePath);
        return JsonConvert.DeserializeObject<List<Person>>(json) ?? new List<Person>();
    }
}
