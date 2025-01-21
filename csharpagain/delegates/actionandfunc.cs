using System;

namespace ConsoleApp20
{
    delegate void Logger(string message);
    class Program
    {
        static void Main()
        {
            // Func zwraca wynik
            Func<int, int, int> add = (a, b) => a + b;
            Console.WriteLine($"5 + 7 = {add(5, 7)}");

            // Action nie zwraca wyniku
            Action<string> printMessage = message => Console.WriteLine($"Message: {message}");
            printMessage("Hello from Action!");
        }
    }
}
