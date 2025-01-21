namespace ConsoleApp20
{
    using System;

    class Program
    {
        static string ValidateAndGreet(string name, int age) => (name, age) switch
        {
            (null, _) => throw new ArgumentNullException(nameof(name)),
            ("", _) => throw new ArgumentException("Imię nie może być puste"),
            (_, < 0) => throw new ArgumentException("Wiek nie może być ujemny"),
            (_, > 120) => throw new ArgumentException("Wiek jest zbyt duży"),
            _ => $"Witaj, {name}! Masz {age} lat."
        };

        static void Main()
        {
            Console.WriteLine(ValidateAndGreet("Anna", 25));  // Witaj, Anna! Masz 25 lat.
            Console.WriteLine(ValidateAndGreet("", 25));      // Wyjątek: Imię nie może być puste
        }
    }

}