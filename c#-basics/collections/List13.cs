using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 1,2,3};
            numbers.Reverse();
            foreach(int num in numbers)
            {
                Console.WriteLine(num); //3,2,1
            }
        }
    }
}
