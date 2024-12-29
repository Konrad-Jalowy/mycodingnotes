using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 1,2,3,7,8,9 };
            List<int> sublist = new List<int>() { 4, 5, 6 };
            bool numbersGreaterThanThree = numbers.TrueForAll(x => x > 3);
            Console.WriteLine(numbersGreaterThanThree); //False
            bool sublistGreaterThanThree = sublist.TrueForAll(x => x > 3);
            Console.WriteLine(sublistGreaterThanThree); //True
        }
    }
}
