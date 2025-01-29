using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        List<string> names1 = new List<string> { "Adam", "Ewa" };
        List<string> names2 = new List<string> { "Marek", "Basia" };

        var combined = names1.Concat(names2);

        Console.WriteLine("Połączone listy: " + string.Join(", ", combined));
    }
}
