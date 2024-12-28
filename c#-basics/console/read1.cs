using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hit any key");
            int key = Console.Read();
            Console.WriteLine(key);
            Console.WriteLine(Convert.ToChar(key));
        }
    }
}
