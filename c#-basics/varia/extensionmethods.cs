namespace ConsoleApp18
{
    public static class IntExtensions
    {
        // Definicja metody rozszerzającej
        public static bool IsEven(this int number)
        {
            return number % 2 == 0;
        }
    }

    class Program
    {
        static void Main()
        {
            int value = 42;

            // Użycie metody rozszerzającej
            Console.WriteLine(value.IsEven()); // True
        }
    }
}