namespace ConsoleApp13
{
    class Program
    {
        
        static void Main(string[] args)
        {
            var numbers = new[] { 1, 2, 3, 4, 5, 6 };

            bool isAnyLargetThanFive = numbers.Any(n => n > 5);

            Console.WriteLine(isAnyLargetThanFive); //True

        }
    }
}
