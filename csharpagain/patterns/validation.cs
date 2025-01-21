namespace ConsoleApp20
{

    using System;

    namespace ConsoleApp20
    {
        class Program
        {
            static void Main()
            {
                object input = "123";

                // Sprawdzamy, czy input jest stringiem
                if (input is string text && text.Length > 0 && text.Length < 10 && int.TryParse(text, out int number))
                {
                    Console.WriteLine($"Poprawne dane: {number}");
                }
                else
                {
                    Console.WriteLine("Niepoprawne dane wejściowe.");
                }
            }
        }
    }


}