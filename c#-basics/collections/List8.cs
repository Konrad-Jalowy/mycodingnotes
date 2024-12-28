using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 10, 2, 3, 6, 42, 5 };
            Console.WriteLine(numbers.Contains(10)); //True
            Console.WriteLine(numbers.Contains(5)); //True
            Console.WriteLine(numbers.Contains(6)); //True
            Console.WriteLine(numbers.Contains(41)); //False
        }
    }
}
