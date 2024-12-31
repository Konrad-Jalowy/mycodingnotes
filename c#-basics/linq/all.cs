namespace ConsoleApp13
{
    class Program
    {
        
        static void Main(string[] args)
        {
            var numbers = new[] { 1, 2, 3, 4, 5, 6 };

            bool allGreaterThanFive = numbers.All(n => n > 5);
            bool allLessThanTen = numbers.All(n => n < 10);

            Console.WriteLine(allGreaterThanFive); //False
            Console.WriteLine(allLessThanTen); //True
        }
    }
}
