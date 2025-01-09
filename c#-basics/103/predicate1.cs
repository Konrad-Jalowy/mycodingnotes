namespace ConsoleApp18
{
    class Program
    {
        static void Main(string[] args)
        {
            Predicate<int> isEven = x => x % 2 == 0;

            Console.WriteLine(isEven(4)); // True
            Console.WriteLine(isEven(7)); // False
        }
    }
}