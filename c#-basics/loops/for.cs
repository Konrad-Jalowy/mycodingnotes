using System;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            for (int counter = 1; counter <= 10; counter++)
            {
                Console.WriteLine("Counter is " + counter);
                Console.ReadKey();
            }

            Console.ReadKey();
        }
    }
}
