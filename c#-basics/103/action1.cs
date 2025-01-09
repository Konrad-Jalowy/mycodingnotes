namespace ConsoleApp18
{
    class Program
    {
        static void Main(string[] args)
        {
            Action greet = () => Console.WriteLine("Cześć, świecie!");
            greet(); // Wyświetli: Cześć, świecie!

            // Action z jednym argumentem
            Action<string> sayHello = name => Console.WriteLine($"Cześć, {name}!");
            sayHello("Janek"); // Wyświetli: Cześć, Janek!

            // Action z dwoma argumentami
            Action<int, int> addAndPrint = (x, y) => Console.WriteLine($"Suma: {x + y}");
            addAndPrint(5, 7); // Wyświetli: Suma: 12
        }
    }
}