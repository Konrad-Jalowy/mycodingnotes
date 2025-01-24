using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        SortedDictionary<string, int> ageDict = new SortedDictionary<string, int>();

        ageDict["Charlie"] = 35;
        ageDict["Alice"] = 25;
        ageDict["Bob"] = 30;

        Console.WriteLine("SortedDictionary:");
        foreach (var entry in ageDict)
        {
            Console.WriteLine($"Klucz: {entry.Key}, Wartość: {entry.Value}");
        }
    }
}
