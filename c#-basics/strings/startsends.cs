using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            string s1 = "hello world";
            if (s1.StartsWith("hello"))
            {
                Console.WriteLine("s1 starts with hello");
            }
            if (s1.EndsWith("world"))
            {
                Console.WriteLine("s1 ends with world");
            }
        }
    }
}
