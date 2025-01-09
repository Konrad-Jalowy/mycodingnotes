using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };

        // LINQ zwraca IEnumerable<int>
        IEnumerable<int> evenNumbers = numbers.Where(n => n % 2 == 0);

        foreach (var num in evenNumbers)
        {
            Console.WriteLine(num); // Wyjście: 2, 4
        }
    }
}
