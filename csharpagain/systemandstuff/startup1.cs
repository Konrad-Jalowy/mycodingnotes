namespace ConsoleApp20
{
    using System;
    using System.IO;

    class Program
    {
        static void Main()
        {
            // Pobranie ścieżki do folderu Startup
            string startupFolder = Environment.GetFolderPath(Environment.SpecialFolder.Startup);

            Console.WriteLine($"Zawartość folderu Startup: {startupFolder}");
            Console.WriteLine();

            // Sprawdzenie, czy folder istnieje
            if (Directory.Exists(startupFolder))
            {
                // Pobranie wszystkich plików w folderze Startup
                string[] files = Directory.GetFiles(startupFolder);

                if (files.Length == 0)
                {
                    Console.WriteLine("Brak plików w folderze Startup.");
                }
                else
                {
                    // Wyświetlenie plików
                    foreach (string file in files)
                    {
                        Console.WriteLine(Path.GetFileName(file));
                    }
                }
            }
            else
            {
                Console.WriteLine("Folder Startup nie istnieje.");
            }

            Console.WriteLine("\nNaciśnij Enter, aby zakończyć...");
            Console.ReadLine();
        }
    }

}