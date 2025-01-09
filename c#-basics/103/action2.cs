namespace ConsoleApp18
{
    class Program
    {
        static void Main(string[] args)
        {
            Action<string> logger = message => Console.WriteLine($"LOG: {message}");

            // Logowanie na konsolę
            logger("Aplikacja wystartowała"); // LOG: Aplikacja wystartowała

            // Zmiana zachowania logowania - zapis do pliku
            logger = message => System.IO.File.AppendAllText("log.txt", $"{message}\n");
            logger("To zostanie zapisane do pliku");

            // Sprawdzenie zawartości pliku
            Console.WriteLine(System.IO.File.ReadAllText("log.txt")); // To zostanie zapisane do pliku
        }
    }
}