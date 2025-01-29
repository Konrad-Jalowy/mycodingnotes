using System;
using System.Linq;
using System.Xml.Linq;

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
        string filePath = "dane.xml";

        // Wczytujemy XML i przekształcamy na listę obiektów
        XDocument xmlDoc = XDocument.Load(filePath);

        var people = xmlDoc.Descendants("Person")
                           .Select(x => new Person
                           {
                               Id = (int)x.Element("Id"),
                               Name = (string)x.Element("Name"),
                               Age = (int)x.Element("Age")
                           })
                           .ToList();

        // Filtrujemy osoby młodsze niż 30 lat
        var youngerThan30 = people.Where(p => p.Age < 30).OrderBy(p => p.Name);

        Console.WriteLine("Osoby młodsze niż 30 lat:");
        foreach (var person in youngerThan30)
        {
            Console.WriteLine($"{person.Name}, {person.Age} lat");
        }
    }
}
