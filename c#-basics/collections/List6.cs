using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 10, 2, 3, 6, 42, 5 };
            numbers.Sort();
            Console.WriteLine(numbers.BinarySearch(5)); //2
            Console.WriteLine(numbers.BinarySearch(6)); //3
            Console.WriteLine(numbers.BinarySearch(41)); //-6
        }
    }
}
