using System;
using System.Linq;
using System.Collections.Generic;

class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
}

class PersonComparer : IEqualityComparer<Person>
{
    public bool Equals(Person x, Person y)
    {
        return x.Name == y.Name && x.Age == y.Age;
    }

    public int GetHashCode(Person obj)
    {
        return obj.Name.GetHashCode() ^ obj.Age.GetHashCode();
    }
}

class Program
{
    static void Main()
    {
        HashSet<Person> people = new HashSet<Person>(new PersonComparer())
        {
            new Person { Name = "Anna", Age = 25 },
            new Person { Name = "Bartek", Age = 30 }
        };

        bool added = people.Add(new Person { Name = "Anna", Age = 25 });

        Console.WriteLine($"Czy dodano duplikat? {added}"); // False
    }
}