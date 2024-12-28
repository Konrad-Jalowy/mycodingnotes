using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.BackgroundColor = ConsoleColor.Blue;
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine("White on blue.");
            Console.WriteLine("Another line.");
            Console.ResetColor();
        }
    }
}
