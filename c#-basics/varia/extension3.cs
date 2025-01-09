namespace ConsoleApp18
{
    public static class ListExtensions
    {
        // Rozszerzanie kolekcji
        public static void PrintAll<T>(this IEnumerable<T> items)
        {
            foreach (var item in items)
            {
                Console.WriteLine(item);
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var numbers = new List<int> { 1, 2, 3, 4, 5 };

            // Użycie metody rozszerzającej
            numbers.PrintAll();
        }
    }
}