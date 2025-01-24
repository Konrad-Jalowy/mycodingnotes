using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Tworzenie SortedDictionary z własnym komparatorem (odwrotna kolejność)
        SortedDictionary<string, int> ageDict = new SortedDictionary<string, int>(Comparer<string>.Create((x, y) => y.CompareTo(x)));

        ageDict["Charlie"] = 35;
        ageDict["Alice"] = 25;
        ageDict["Bob"] = 30;

        Console.WriteLine("SortedDictionary z odwrotną kolejnością:");
        foreach (var entry in ageDict)
        {
            Console.WriteLine($"Klucz: {entry.Key}, Wartość: {entry.Value}");
        }
    }
}
