namespace Program123
{
    using System;
    using System.IO;
    using System.Text;

    class Program
    {
        static void Main()
        {
            // Rejestracja dostawcy kodowań dla obsługi stron kodowych
            Encoding.RegisterProvider(CodePagesEncodingProvider.Instance);

            // Pobranie ścieżki pulpitu
            string desktopPath = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);

            // Zapytanie użytkownika o nazwę pliku
            Console.Write("Podaj nazwę pliku (bez lub z .txt): ");
            string fileName = Console.ReadLine()?.Trim();

            // Dodanie rozszerzenia .txt, jeśli brak
            if (!fileName.EndsWith(".txt", StringComparison.OrdinalIgnoreCase))
            {
                fileName += ".txt";
            }

            // Pełna ścieżka pliku
            string filePath = Path.Combine(desktopPath, fileName);

            // Sprawdzenie, czy plik istnieje
            if (!File.Exists(filePath))
            {
                Console.WriteLine($"Plik '{filePath}' nie istnieje na pulpicie.");
                return;
            }

            try
            {
                // Odczytanie bajtów z pliku
                byte[] fileBytes = File.ReadAllBytes(filePath);

                // Wykrywanie kodowania
                Encoding detectedEncoding = DetectEncoding(fileBytes);

                Console.WriteLine($"Wykryte kodowanie: {detectedEncoding.WebName}");

                // Sprawdzenie, czy UTF-8 zawiera BOM
                if (detectedEncoding.WebName.Equals("utf-8", StringComparison.OrdinalIgnoreCase))
                {
                    bool hasBom = HasUtf8Bom(fileBytes);
                    Console.WriteLine($"UTF-8 BOM: {(hasBom ? "Tak" : "Nie")}");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Wystąpił błąd: {ex.Message}");
            }
        }

        // Metoda do wykrywania kodowania
        static Encoding DetectEncoding(byte[] fileBytes)
        {
            // Sprawdzenie, czy plik ma BOM
            if (fileBytes.Length >= 3 &&
                fileBytes[0] == 0xEF && fileBytes[1] == 0xBB && fileBytes[2] == 0xBF)
            {
                return Encoding.UTF8; // UTF-8 z BOM
            }
            else if (fileBytes.Length >= 2 &&
                     fileBytes[0] == 0xFF && fileBytes[1] == 0xFE)
            {
                return Encoding.Unicode; // UTF-16 LE z BOM
            }
            else if (fileBytes.Length >= 2 &&
                     fileBytes[0] == 0xFE && fileBytes[1] == 0xFF)
            {
                return Encoding.BigEndianUnicode; // UTF-16 BE z BOM
            }

            // Próba wykrycia innych kodowań za pomocą Encoding.Default
            // Można użyć bardziej zaawansowanych bibliotek do detekcji
            return Encoding.Default;
        }

        // Metoda do sprawdzenia obecności BOM w UTF-8
        static bool HasUtf8Bom(byte[] fileBytes)
        {
            return fileBytes.Length >= 3 &&
                   fileBytes[0] == 0xEF && fileBytes[1] == 0xBB && fileBytes[2] == 0xBF;
        }
    }

}