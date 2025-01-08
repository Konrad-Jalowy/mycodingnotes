namespace ConsoleApp18
{
    using System.Threading.Tasks;

    class Program
    {
        static void Main()
        {
            // Symulacja obrazów: każdy obraz to tablica 1000 pikseli
            int numberOfImages = 10; // Liczba obrazów
            int imageSize = 1000;    // Liczba pikseli w jednym obrazie
            int[][] images = new int[numberOfImages][];

            Random random = new Random();

            // Generowanie losowych pikseli dla obrazów
            for (int i = 0; i < numberOfImages; i++)
            {
                images[i] = new int[imageSize];
                for (int j = 0; j < imageSize; j++)
                {
                    images[i][j] = random.Next(0, 256); // Losowe wartości pikseli 0-255
                }
            }

            // Zwiększenie jasności za pomocą Parallel.For
            Console.WriteLine("Przetwarzanie obrazów równolegle...");
            Parallel.For(0, numberOfImages, i =>
            {
                // Dla każdego obrazu przetwarzamy piksele
                for (int j = 0; j < images[i].Length; j++)
                {
                    // Zwiększenie jasności pikseli (z ograniczeniem do 255)
                    images[i][j] = Math.Min(images[i][j] + 10, 255);
                }
            });

            Console.WriteLine("Przetwarzanie zakończone.");

            // Wyświetlenie kilku wyników (dla celów demonstracyjnych)
            Console.WriteLine("\nPrzykładowe wyniki:");
            for (int i = 0; i < 3; i++) // Wyświetlamy 3 obrazy
            {
                Console.WriteLine($"Obraz {i + 1}, piksele: {string.Join(", ", images[i][..10])}...");
            }
        }
    }
}
