using System;

namespace ConsoleApp20
{
    delegate void SimpleDelegate(string message);
    class Program
    {
        static void Main()
        {
            // Przypisanie metody do delegatu
            SimpleDelegate del = DisplayMessage;

            // Wywołanie delegatu
            del("Hello, World!");
        }

        static void DisplayMessage(string message)
        {
            Console.WriteLine(message);
        }
    }
}
