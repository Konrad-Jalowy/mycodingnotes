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
            foreach(KeyValuePair<int, string> item in people)
            {
                Console.WriteLine(item.Key + " : " + item.Value);
            }
        }
      
    }
      
}
