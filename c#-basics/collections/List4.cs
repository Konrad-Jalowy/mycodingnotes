using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 1, 2, 3, 4, 5 };
            foreach(int number in numbers)
            {
                Console.WriteLine(number);
            }
        }
    }
}
