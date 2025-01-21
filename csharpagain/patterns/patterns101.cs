namespace ConsoleApp20
{
    using System;

    class Program
    {
        static void Main()
        {
            object obj = 42;

            switch (obj)
            {
                case int number when number > 0:
                    Console.WriteLine($"Dodatnia liczba: {number}");
                    break;
                case int number:
                    Console.WriteLine($"Inna liczba całkowita: {number}");
                    break;
                case string text:
                    Console.WriteLine($"Tekst: {text}");
                    break;
                default:
                    Console.WriteLine("Nieznany typ");
                    break;
            }
        }
    }
}