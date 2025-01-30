using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };

        var squaredNumbers = from n in numbers
                             select n * n;

        Console.WriteLine(string.Join(", ", squaredNumbers));
    }
}
