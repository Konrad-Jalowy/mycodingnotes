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
        string csvFilePath = "dane.csv";
        string xmlFilePath = "dane.xml";
        string jsonFilePath = "dane.json";

        // Wczytanie danych z JSON lub CSV
        var people = ReadFromJson(jsonFilePath);
        if (!people.Any())
        {
            people = ReadFromCsv(csvFilePath);
        }

        Console.WriteLine("Dane wczytane.");

        // Interaktywne dodawanie nowych rekordów
        while (true)
        {
            Console.WriteLine("Czy chcesz dodać nową osobę? (tak/nie)");
            string input = Console.ReadLine()?.Trim().ToLower();
            if (input != "tak") break;

            Console.Write("Podaj ID: ");
            int id = int.Parse(Console.ReadLine());

            Console.Write("Podaj imię: ");
            string name = Console.ReadLine();

            Console.Write("Podaj wiek: ");
            int age = int.Parse(Console.ReadLine());

            people.Add(new Person { Id = id, Name = name, Age = age });
        }

        // Interaktywne usuwanie rekordów
        while (true)
        {
            Console.WriteLine("Czy chcesz usunąć osobę? (tak/nie)");
            string input = Console.ReadLine()?.Trim().ToLower();
            if (input != "tak") break;

            Console.Write("Podaj ID osoby do usunięcia: ");
            int id = int.Parse(Console.ReadLine());

            var personToRemove = people.FirstOrDefault(p => p.Id == id);
            if (personToRemove != null)
            {
                people.Remove(personToRemove);
                Console.WriteLine("Osoba usunięta.");
            }
            else
            {
                Console.WriteLine("Nie znaleziono osoby o podanym ID.");
            }
        }

        // Zapisanie danych do XML
        SaveToXml(xmlFilePath, people);
        Console.WriteLine("Dane zapisane do XML.");

        // Zapisanie danych do JSON
        SaveToJson(jsonFilePath, people);
        Console.WriteLine("Dane zapisane do JSON.");
    }

    static List<Person> ReadFromCsv(string filePath)
    {
        if (!File.Exists(filePath)) return new List<Person>();
        return File.ReadAllLines(filePath)
                   .Skip(1) // Pomijamy nagłówek
                   .Select(line => line.Split(','))
                   .Select(parts => new Person
                   {
                       Id = int.Parse(parts[0]),
                       Name = parts[1],
                       Age = int.Parse(parts[2])
                   })
                   .ToList();
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
