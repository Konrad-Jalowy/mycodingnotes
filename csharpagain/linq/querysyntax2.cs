using System;
using System.Collections.Generic;
using System.Linq;

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

        var names = from p in people
                    select p.Name;

        Console.WriteLine(string.Join(", ", names));
    }
}
