using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 4,5,6 };
            numbers.Insert(0, 3);
            numbers.Insert(0, 2);
            numbers.Insert(0, 1);
            numbers.Insert(0, 0);
            foreach (int number in numbers)
            {
                Console.WriteLine(number); //0,1,2,3,4,5,6
            }
        }
    }
}
