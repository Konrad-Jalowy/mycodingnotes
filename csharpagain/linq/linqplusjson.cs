using System;
using System.Linq;
using System.Collections.Generic;
using Newtonsoft.Json;

class Program
{
    class Person
    {
        public string Name { get; set; }
        public int Age { get; set; }
    }

    static void Main()
    {
        string json = "[{\"Name\": \"Adam\", \"Age\": 30}, {\"Name\": \"Ewa\", \"Age\": 25}, {\"Name\": \"Marek\", \"Age\": 40}]";
        
        var people = JsonConvert.DeserializeObject<List<Person>>(json);
        var adults = people.Where(p => p.Age > 25);

        foreach (var person in adults)
        {
            Console.WriteLine($"{person.Name}, {person.Age} lat");
        }
    }
}
