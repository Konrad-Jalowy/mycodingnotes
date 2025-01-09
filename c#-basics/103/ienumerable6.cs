using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };

        // IEnumerable jako pośredni typ
        IEnumerable<int> enumerable = numbers.Where(n => n % 2 == 0);

        // Konwersja z powrotem do List<int>
        List<int> evenNumbers = enumerable.ToList();

        Console.WriteLine(string.Join(", ", evenNumbers)); // Wyjście: 2, 4
    }
}
