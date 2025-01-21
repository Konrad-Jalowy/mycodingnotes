using System;

namespace ConsoleApp20
{
    delegate void MultiDelegate(string message);
    class Program
    {
        static void Main()
        {
            MultiDelegate del = Method1;
            del += Method2; // Dodanie kolejnej metody

            // Wywołanie delegatu (wywoła obie metody w kolejności)
            del("Hello!");
        }

        static void Method1(string message)
        {
            Console.WriteLine($"Method1: {message}");
        }

        static void Method2(string message)
        {
            Console.WriteLine($"Method2: {message}");
        }
    }
}

