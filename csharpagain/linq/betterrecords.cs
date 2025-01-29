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

        while (true)
        {
            Console.WriteLine("\nWybierz opcję:");
            Console.WriteLine("1. Wyświetl wszystkie osoby");
            Console.WriteLine("2. Wyświetl osobę po ID");
            Console.WriteLine("3. Dodaj osobę");
            Console.WriteLine("4. Edytuj osobę");
            Console.WriteLine("5. Usuń osobę");
            Console.WriteLine("6. Zapisz do CSV");
            Console.WriteLine("7. Zapisz do XML");
            Console.WriteLine("8. Wyjdź");
            Console.Write("Twój wybór: ");

            string choice = Console.ReadLine();
            switch (choice)
            {
                case "1":
                    DisplayAll(people);
                    break;
                case "2":
                    DisplaySingle(people);
                    break;
                case "3":
                    AddPerson(people);
                    break;
                case "4":
                    EditPerson(people);
                    break;
                case "5":
                    RemovePerson(people);
                    break;
                case "6":
                    SaveToCsv("output.csv", people);
                    Console.WriteLine("Dane zapisane do CSV.");
                    break;
                case "7":
                    SaveToXml("output.xml", people);
                    Console.WriteLine("Dane zapisane do XML.");
                    break;
                case "8":
                    SaveToJson(jsonFilePath, people);
                    return;
                default:
                    Console.WriteLine("Niepoprawna opcja.");
                    break;
            }
        }
    }

    static void DisplayAll(List<Person> people)
    {
        foreach (var p in people)
            Console.WriteLine($"ID: {p.Id}, Imię: {p.Name}, Wiek: {p.Age}");
    }

    static void DisplaySingle(List<Person> people)
    {
        Console.Write("Podaj ID osoby: ");
        int id = int.Parse(Console.ReadLine());
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

    static void EditPerson(List<Person> people)
    {
        Console.Write("Podaj ID osoby do edycji: ");
        int id = int.Parse(Console.ReadLine());
        var person = people.FirstOrDefault(p => p.Id == id);
        if (person != null)
        {
            Console.Write("Nowe imię (pozostaw puste, aby nie zmieniać): ");
            string newName = Console.ReadLine();
            if (!string.IsNullOrWhiteSpace(newName))
                person.Name = newName;
            Console.Write("Nowy wiek (pozostaw puste, aby nie zmieniać): ");
            string newAge = Console.ReadLine();
            if (!string.IsNullOrWhiteSpace(newAge))
                person.Age = int.Parse(newAge);
            Console.WriteLine("Dane osoby zaktualizowane.");
        }
        else
            Console.WriteLine("Nie znaleziono osoby o podanym ID.");
    }

    static void RemovePerson(List<Person> people)
    {
        Console.Write("Podaj ID osoby do usunięcia: ");
        int id = int.Parse(Console.ReadLine());
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
