using System;

namespace ConsoleApp20
{
    delegate void MultiDelegate(string message);
    class Program
    {
        static void Main()
        {
            MultiDelegate del = Method1;
            del += Method2;

            Console.WriteLine("Wywołanie delegatu z obiema metodami:");
            del("Hello!");

            // Usunięcie jednej metody
            del -= Method1;

            Console.WriteLine("Wywołanie delegatu po usunięciu Method1:");
            del("Hello again!");
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
