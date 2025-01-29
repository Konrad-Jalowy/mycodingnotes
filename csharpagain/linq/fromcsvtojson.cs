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

        // Wczytanie danych z CSV
        var people = ReadFromCsv(csvFilePath);
        Console.WriteLine("Dane z CSV wczytane.");

        // Zapisanie danych do XML
        SaveToXml(xmlFilePath, people);
        Console.WriteLine("Dane zapisane do XML.");

        // Zapisanie danych do JSON
        SaveToJson(jsonFilePath, people);
        Console.WriteLine("Dane zapisane do JSON.");
    }

    static List<Person> ReadFromCsv(string filePath)
    {
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
}
