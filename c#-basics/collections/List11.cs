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
            numbers.InsertRange(3, sublist);
           
            foreach (int number in numbers)
            {
                Console.WriteLine(number); //1,2,3,4,5,6,7,8,9
            }
        }
    }
}
