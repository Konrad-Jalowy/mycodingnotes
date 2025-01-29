using System;
using System.IO;
using System.Linq;

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
        string filePath = "dane.csv";

        // Wczytujemy CSV i parsujemy do listy obiektów
        var people = File.ReadAllLines(filePath)
                         .Skip(1) // Pomijamy nagłówek
                         .Select(line => line.Split(','))
                         .Select(parts => new Person
                         {
                             Id = int.Parse(parts[0]),
                             Name = parts[1],
                             Age = int.Parse(parts[2])
                         })
                         .ToList();

        // Filtrujemy osoby starsze niż 30 lat
        var olderThan30 = people.Where(p => p.Age > 30).OrderBy(p => p.Name);

        Console.WriteLine("Osoby starsze niż 30 lat:");
        foreach (var person in olderThan30)
        {
            Console.WriteLine($"{person.Name}, {person.Age} lat");
        }
    }
}
