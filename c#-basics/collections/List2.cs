using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 1, 2, 3, 4, 5 };
            numbers.Add(6);
            numbers.Add(7);
            numbers.Add(8);
            Console.WriteLine(numbers.Count); //8
        }
    }
}
