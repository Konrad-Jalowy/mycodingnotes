namespace ConsoleApp20
{
    using System;

    class Program
    {
        static double Calculator(double a, double b, string operation) => operation switch
        {
            "+" => a + b,
            "-" => a - b,
            "*" => a * b,
            "/" when b != 0 => a / b, // Warunek dodatkowy: dzielenie przez 0
            "/" => throw new DivideByZeroException("Nie można dzielić przez zero"),
            _ => throw new ArgumentException("Nieznana operacja")
        };

        static void Main()
        {
            Console.WriteLine(Calculator(10, 2, "+")); // 12
            Console.WriteLine(Calculator(10, 2, "/")); // 5
            Console.WriteLine(Calculator(10, 2, "-")); // 8
        }
    }


}