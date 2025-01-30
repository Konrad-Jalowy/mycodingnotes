using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };

        // Zmiana każdego elementu
        var squaredNumbers = numbers.Select(n => n * n);

        Console.WriteLine(string.Join(", ", squaredNumbers));
    }
}
