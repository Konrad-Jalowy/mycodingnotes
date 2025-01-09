using System;
using System.Collections.Generic;

class Program
{
    static void PrintElements(IEnumerable<string> elements)
    {
        foreach (var element in elements)
        {
            Console.WriteLine(element);
        }
    }

    static void Main()
    {
        var list = new List<string> { "Apple", "Banana", "Cherry" };
        string[] array = { "Dog", "Cat", "Bird" };

        // Metoda przyjmuje różne typy kolekcji dzięki IEnumerable
        PrintElements(list);
        PrintElements(array);
    }
}
