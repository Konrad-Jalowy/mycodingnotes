using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter your name:> ");
            string username = Console.ReadLine();
            Console.WriteLine($"Hello {username}!");
        }
    }
}
