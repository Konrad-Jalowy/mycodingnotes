namespace ConsoleApp20
{
    using System;
    using System.IO;

    class Program
    {
        static void Main()
        {
            string folderPath = @"C:\watchme"; // Podaj ścieżkę do katalogu

            if (!Directory.Exists(folderPath))
            {
                Console.WriteLine("Podany katalog nie istnieje.");
                return;
            }

            using var watcher = new FileSystemWatcher(folderPath);

            // Konfiguracja zdarzeń
            watcher.NotifyFilter = NotifyFilters.FileName | NotifyFilters.LastWrite | NotifyFilters.CreationTime;

            watcher.Changed += OnChanged;  // Plik zmieniony
            watcher.Created += OnCreated; // Plik utworzony
            watcher.Deleted += OnDeleted; // Plik usunięty
            watcher.Renamed += OnRenamed; // Plik zmieniono nazwę

            // Monitoruj wszystkie pliki
            watcher.Filter = "*.*";

            // Włącz monitorowanie podkatalogów
            watcher.IncludeSubdirectories = true;

            // Start monitorowania
            watcher.EnableRaisingEvents = true;

            Console.WriteLine($"Monitoring folderu: {folderPath}");
            Console.WriteLine("Naciśnij [Enter], aby zakończyć...");
            Console.ReadLine();
        }

        private static void OnChanged(object sender, FileSystemEventArgs e)
        {
            Console.WriteLine($"[Zmieniono] {e.FullPath}");
        }

        private static void OnCreated(object sender, FileSystemEventArgs e)
        {
            Console.WriteLine($"[Utworzono] {e.FullPath}");
        }

        private static void OnDeleted(object sender, FileSystemEventArgs e)
        {
            Console.WriteLine($"[Usunięto] {e.FullPath}");
        }

        private static void OnRenamed(object sender, RenamedEventArgs e)
        {
            Console.WriteLine($"[Zmieniono nazwę] {e.OldFullPath} -> {e.FullPath}");
        }
    }


}