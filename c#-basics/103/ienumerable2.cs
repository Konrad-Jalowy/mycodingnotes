using System;
using System.Collections.Generic;

class Program
{
    static IEnumerable<int> GenerateNumbers()
    {
        for (int i = 1; i <= 5; i++)
        {
            yield return i; // Każdy element jest generowany w locie
        }
    }

    static void Main()
    {
        foreach (var number in GenerateNumbers())
        {
            Console.WriteLine(number); // Wyjście: 1, 2, 3, 4, 5
        }
    }
}
