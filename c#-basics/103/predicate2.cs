namespace ConsoleApp18
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int> { 1, 2, 3, 4, 5, 6 };

            // Predicate do sprawdzania liczb parzystych
            Predicate<int> isEven = x => x % 2 == 0;

            // Znajdź pierwszą liczbę parzystą
            int firstEven = numbers.Find(isEven);
            Console.WriteLine(firstEven); // 2

            // Znajdź wszystkie liczby parzyste
            List<int> evenNumbers = numbers.FindAll(isEven);
            Console.WriteLine(string.Join(", ", evenNumbers)); // 2, 4, 6
        }
    }
}