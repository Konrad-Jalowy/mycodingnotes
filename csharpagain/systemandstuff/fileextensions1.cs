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
            string valueName = "HideFileExt";

            // Sprawdzenie wartości
            int hideFileExtValue = GetRegistryValue(registryPath, valueName);

            // Interpretacja wyniku
            if (hideFileExtValue == 0)
            {
                Console.WriteLine("Rozszerzenia plików są widoczne.");
            }
            else if (hideFileExtValue == 1)
            {
                Console.WriteLine("Rozszerzenia plików są ukryte.");
            }
            else
            {
                Console.WriteLine("Nie można odczytać ustawienia widoczności rozszerzeń.");
            }
        }

        static int GetRegistryValue(string path, string valueName)
        {
            try
            {
                using (var key = Registry.CurrentUser.OpenSubKey(path))
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
                Console.WriteLine($"Błąd podczas odczytu rejestru: {ex.Message}");
            }

            return -1; // Wartość -1 oznacza błąd lub brak wpisu
        }
    }

}