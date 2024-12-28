using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 10, 2, 3, 6, 42, 5 };
            Console.WriteLine(numbers.IndexOf(10)); //0
            Console.WriteLine(numbers.IndexOf(5)); //5
            Console.WriteLine(numbers.IndexOf(6)); //3
            Console.WriteLine(numbers.IndexOf(41)); //-1
        }
    }
}
