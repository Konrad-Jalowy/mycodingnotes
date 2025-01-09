using System;
using System.Collections.Generic;
using System.Linq;

public static class Extensions
{
    public static int CountGreaterThan(this IEnumerable<int> numbers, int threshold)
    {
        return numbers.Count(n => n > threshold);
    }
}

class Program
{
    static void Main()
    {
        var numbers = new List<int> { 1, 5, 10, 15, 20 };

        // Rozszerzenie działa na każdej kolekcji implementującej IEnumerable<int>
        int count = numbers.CountGreaterThan(10);
        Console.WriteLine(count); // Wyjście: 2
    }
}
