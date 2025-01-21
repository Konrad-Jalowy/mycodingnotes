using System;

namespace ConsoleApp20
{
    delegate void LambdaDelegate(string message);
    class Program
    {
        static void Main()
        {
            LambdaDelegate del = (message) => Console.WriteLine($"Wyrażenie lambda: {message}");

            del("Hello from lambda!");
        }
    }

}
