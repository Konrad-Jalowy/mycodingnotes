namespace ConsoleApp20
{
    using System;
    using Microsoft.Win32;

    class Program
    {
        static void Main()
        {
            // Ścieżka do klucza rejestru
            string registryPath = @"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced";

            // Sprawdzenie ustawień
            int hiddenValue = GetRegistryValue(registryPath, "Hidden");
            int superHiddenValue = GetRegistryValue(registryPath, "ShowSuperHidden");

            // Wyświetlenie wyników
            Console.WriteLine("Widok ukrytych plików i folderów:");
            Console.WriteLine(hiddenValue == 1
                ? "- Ukryte pliki i foldery są widoczne."
                : "- Ukryte pliki i foldery są ukryte.");

            Console.WriteLine(superHiddenValue == 1
                ? "- Chronione pliki systemowe są widoczne."
                : "- Chronione pliki systemowe są ukryte.");

            Console.WriteLine("\nNaciśnij Enter, aby zakończyć...");
            Console.ReadLine();
        }

        static int GetRegistryValue(string path, string valueName)
        {
            try
            {
                using (RegistryKey key = Registry.CurrentUser.OpenSubKey(path))
                {
                    if (key != null)
                    {
                        object value = key.GetValue(valueName);
                        if (value is int intValue)
                        {
                            return intValue;
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Błąd odczytu rejestru: {ex.Message}");
            }

            return -1; // Zwraca -1, jeśli wartość nie została znaleziona
        }
    }
}