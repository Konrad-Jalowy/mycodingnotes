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

            Console.WriteLine(people.ContainsKey(3)); //True
            Console.WriteLine(people.ContainsValue("John Doe")); //True
        }     
    }    
}
