using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 10, 2, 3, 6, 42, 5 };
            numbers.Clear();
            Console.WriteLine(numbers.Count); //0
        }
    }
}
