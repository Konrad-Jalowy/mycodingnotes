using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        List<string> names = new List<string> { "Adam", "Alicja", "Barbara", "Bartosz", "Marek", "Marcin", "Anna" };

        var groupedNames = names.GroupBy(n => n[0]); // Grupowanie po pierwszej literze

        foreach (var group in groupedNames)
        {
            Console.WriteLine($"Litera: {group.Key}");
            foreach (var name in group)
            {
                Console.WriteLine($"  - {name}");
            }
        }
    }
}
