namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            Console.WriteLine("Press Enter to continue!");
            ConsoleKeyInfo input;
            do
            {
                 input = Console.ReadKey();
            } while (input.Key != ConsoleKey.Enter);

            Console.WriteLine("Enter pressed, thanks!");
        }
    }
}
