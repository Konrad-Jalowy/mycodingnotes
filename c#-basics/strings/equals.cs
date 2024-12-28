using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            string s1 = "fox";
            string s2 = "fox";
            if (s1.Equals(s2))
            {
                Console.WriteLine("s1 === s2");
            }
        }
    }
}