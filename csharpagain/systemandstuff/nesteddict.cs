using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Dictionary<string, Dictionary<string, int>> nestedDict = new Dictionary<string, Dictionary<string, int>>();

        // Tworzenie zagnieżdżonych słowników
        nestedDict["Alice"] = new Dictionary<string, int>
        {
            { "Math", 90 },
            { "English", 85 }
        };

        nestedDict["Bob"] = new Dictionary<string, int>
        {
            { "Math", 80 },
            { "Science", 88 }
        };

        // Iteracja po zagnieżdżonych słownikach
        foreach (var outerEntry in nestedDict)
        {
            Console.WriteLine($"Uczeń: {outerEntry.Key}");
            foreach (var innerEntry in outerEntry.Value)
            {
                Console.WriteLine($"  Przedmiot: {innerEntry.Key}, Ocena: {innerEntry.Value}");
            }
        }
    }
}
