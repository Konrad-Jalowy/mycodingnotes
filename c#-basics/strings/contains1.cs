using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            string s1 = "The quick brown fox jumps over the lazy dog";
            string s2 = "fox";
            if (s1.Contains(s2))
            {
                Console.WriteLine("Yes, s1 contains s2");
            }
        }
    }
}
