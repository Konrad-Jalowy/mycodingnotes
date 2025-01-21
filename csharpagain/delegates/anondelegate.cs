using System;

namespace ConsoleApp20
{
    delegate void AnonymousDelegate(string message);
    class Program
    {
        static void Main()
        {
            AnonymousDelegate del = delegate (string message)
            {
                Console.WriteLine($"Anonimowa metoda: {message}");
            };

            del("Hello from anonymous method!");
        }
    }
}
