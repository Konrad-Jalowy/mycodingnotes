using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        List<string> names = new List<string> { "Adam", "Ewa", "Marek" };

        bool hasEwa = names.Any(n => n == "Ewa");
        bool hasBasia = names.Contains("Basia");

        Console.WriteLine($"Czy lista zawiera Ewę? {hasEwa}");
        Console.WriteLine($"Czy lista zawiera Basię? {hasBasia}");
    }
}
