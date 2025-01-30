using System;
using System.Linq;
using System.Collections.Generic;

class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
}

class Program
{
    static void Main()
    {
        List<Person> people = new List<Person>
        {
            new Person { Name = "Anna", Age = 25 },
            new Person { Name = "Bartek", Age = 30 },
            new Person { Name = "Celina", Age = 22 }
        };

        var groupedByAge = people.GroupBy(p => p.Age);

        foreach (var group in groupedByAge)
        {
            Console.WriteLine($"Wiek: {group.Key}");
            foreach (var person in group)
            {
                Console.WriteLine($" - {person.Name}");
            }
        }
    }
}
