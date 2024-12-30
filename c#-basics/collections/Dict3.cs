using System;
using System.Collections.Generic;
namespace ConsoleApp12
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<int, string> people = new Dictionary<int, string>()
            {
                {1, "John Doe" },
                {2, "Jane Doe" },
                {3, "Jim Doe" }
            };

            Dictionary<int, string>.KeyCollection keys = people.Keys;

            foreach(int k in keys)
            {
                Console.WriteLine(people[k]);
            }
        }     
    }    
}
