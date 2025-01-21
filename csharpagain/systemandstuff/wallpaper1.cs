namespace ConsoleApp20
{
    using System;
    using Microsoft.Win32;

    class Program
    {
        static void Main()
        {
            string registryPath = @"Control Panel\Desktop";
            string wallpaper = GetRegistryValue(registryPath, "Wallpaper");
            Console.WriteLine($"Aktualna tapeta: {wallpaper}");
        }

        static string GetRegistryValue(string path, string valueName)
        {
            using (var key = Registry.CurrentUser.OpenSubKey(path))
            {
                return key?.GetValue(valueName)?.ToString() ?? "Nie znaleziono wartości";
            }
        }
    }

}