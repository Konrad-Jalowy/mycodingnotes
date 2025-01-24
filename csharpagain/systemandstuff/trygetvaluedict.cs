using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Dictionary<string, int> ageDict = new Dictionary<string, int>
        {
            { "Alice", 25 },
            { "Bob", 30 }
        };

        // Próba pobrania wartości
        if (ageDict.TryGetValue("Charlie", out int age))
        {
            Console.WriteLine($"Wiek Charlie: {age}");
        }
        else
        {
            Console.WriteLine("Charlie nie istnieje w słowniku.");
        }
    }
}
