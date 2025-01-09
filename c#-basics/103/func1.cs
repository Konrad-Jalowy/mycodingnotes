using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp18
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };

            Func<int, bool> isEven = x => x % 2 == 0;

            var evenNumbers = numbers.Where(isEven);
            Console.WriteLine(string.Join(", ", evenNumbers)); // 2, 4
        }
    }
}