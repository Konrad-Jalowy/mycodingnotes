namespace Program123
{
    using System;
    using System.IO;
    using System.Text;

    class TextFileSaver
    {
        static void Main(string[] args)
        {
            // Rejestracja dostawcy kodowań
            Encoding.RegisterProvider(CodePagesEncodingProvider.Instance);

            // 1. Wprowadzanie tekstu linijka po linijce
            Console.WriteLine("Wprowadzaj linijki tekstu. Wpisz '\\end' na końcu, aby zakończyć.");
            var lines = new System.Collections.Generic.List<string>();

            while (true)
            {
                string input = Console.ReadLine();
                if (input.Trim().Equals("\\end", StringComparison.OrdinalIgnoreCase))
                    break;
                lines.Add(input);
            }

            // 2. Pobieranie nazwy pliku
            Console.Write("Podaj nazwę pliku (bez rozszerzenia): ");
            string fileName = Console.ReadLine();

            // 3. Wybór kodowania
            Console.WriteLine("Wybierz kodowanie pliku:");
            Console.WriteLine("1 - ASCII");
            Console.WriteLine("2 - UTF-8");
            Console.WriteLine("3 - UTF-16");
            Console.WriteLine("4 - Windows-1250");
            Console.Write("Twój wybór: ");
            int choice = int.Parse(Console.ReadLine());

            Encoding encoding;
            switch (choice)
            {
                case 1:
                    encoding = Encoding.ASCII;
                    break;
                case 2:
                    encoding = Encoding.UTF8;
                    break;
                case 3:
                    encoding = Encoding.Unicode;
                    break;
                case 4:
                    encoding = Encoding.GetEncoding("windows-1250");
                    break;
                default:
                    Console.WriteLine("Nieprawidłowy wybór. Używam UTF-8 jako domyślnego.");
                    encoding = Encoding.UTF8;
                    break;
            }

            // 4. Tworzenie ścieżki pliku na pulpicie
            string desktopPath = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
            string filePath = Path.Combine(desktopPath, fileName + ".txt");

            // 5. Zapisywanie pliku
            try
            {
                File.WriteAllLines(filePath, lines, encoding);
                Console.WriteLine($"Plik został zapisany na pulpicie: {filePath} w kodowaniu {encoding.WebName}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Wystąpił błąd podczas zapisywania pliku: {ex.Message}");
            }
        }
    }


}