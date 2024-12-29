using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 1,2,3};
            int notOdd = numbers.Find(x => x % 2 == 0);
            Console.WriteLine(notOdd); //2
        }
    }
}
