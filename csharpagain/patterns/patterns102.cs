using System;

namespace ConsoleApp20
{
   class Program
    {
        static void Main()
        {
            object obj = "Hello, Pattern Matching!";

            if (obj is string text)
            {
                Console.WriteLine($"Długość tekstu: {text.Length}");
            }
            else if (obj is int number)
            {
                Console.WriteLine($"Liczba: {number}");
            }
            else
            {
                Console.WriteLine("Nieznany typ");
            }
        }
    }
}