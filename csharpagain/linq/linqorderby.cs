using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        List<int> numbers = new List<int> { 5, 1, 4, 3, 2 };

        // Sortowanie rosnące
        var ascending = numbers.OrderBy(n => n);
        Console.WriteLine("Rosnąco: " + string.Join(", ", ascending));

        // Sortowanie malejące
        var descending = numbers.OrderByDescending(n => n);
        Console.WriteLine("Malejąco: " + string.Join(", ", descending));
    }
}
