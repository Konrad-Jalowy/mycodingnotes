using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        List<int> numbers = new List<int> { 1, 2, 3, 3, 4, 5, 5, 6 };

        var uniqueNumbers = numbers.Distinct();

        Console.WriteLine("Unikalne liczby: " + string.Join(", ", uniqueNumbers));
    }
}
