namespace ConsoleApp20
{
    class Program
    {
        static int Factorial(int n) => n switch
        {
            0 => 1,
            > 0 => n * Factorial(n - 1),
            _ => throw new ArgumentException("Liczba musi być >= 0")
        };

        static void Main()
        {
            Console.WriteLine($"5! = {Factorial(5)}");
        }
    }
}