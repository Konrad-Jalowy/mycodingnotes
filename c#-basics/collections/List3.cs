using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 1, 2, 3, 4, 5 };
            List<int> sublist = new List<int>() { 9, 10, 11 };
            numbers.Add(6);
            numbers.Add(7);
            numbers.Add(8);
            numbers.AddRange(sublist);
            Console.WriteLine(numbers.Count); //11
        }
    }
}
