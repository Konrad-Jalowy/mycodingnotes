using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var names = new List<string> { "Anna", "Bartek", "Celina" };
        var ages = new List<int> { 25, 30, 22 };

        var people = names.Zip(ages, (name, age) => $"{name} ma {age} lat");

        foreach (var person in people)
        {
            Console.WriteLine(person);
        }
    }
}
