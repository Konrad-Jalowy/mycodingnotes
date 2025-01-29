using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        List<int> numbers = new List<int> { 10, 20, 30, 40 };

        int sum = numbers.Sum();
        double average = numbers.Average();
        int min = numbers.Min();
        int max = numbers.Max();

        Console.WriteLine($"Suma: {sum}, Średnia: {average}, Min: {min}, Max: {max}");
    }
}
