using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        List<int> numbers = new List<int> { 3, 8, 2, 7, 1, 9, 6 };

        var top3 = numbers.OrderByDescending(n => n).Take(3);

        Console.WriteLine("Top 3 największe liczby: " + string.Join(", ", top3));
    }
}
