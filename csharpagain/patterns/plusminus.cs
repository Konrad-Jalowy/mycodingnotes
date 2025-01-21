namespace ConsoleApp20
{
    class Program
    {
        static void Main()
        {
            var operation = (3, "+", 5);

            string result = operation switch
            {
                (int a, "+", int b) => $"{a} + {b} = {a + b}",
                (int a, "-", int b) => $"{a} - {b} = {a - b}",
                _ => "Nieznana operacja"
            };

            Console.WriteLine(result);
        }
    }
}
