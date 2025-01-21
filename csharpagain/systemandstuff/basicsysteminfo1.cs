namespace ConsoleApp20
{
    using System;
    using Microsoft.Win32;

    class Program
    {
        static void Main()
        {
            string registryPath = @"SOFTWARE\Microsoft\Windows NT\CurrentVersion";

            string productName = GetRegistryValue(registryPath, "ProductName");
            string buildNumber = GetRegistryValue(registryPath, "CurrentBuild");

            Console.WriteLine($"System operacyjny: {productName}");
            Console.WriteLine($"Numer kompilacji: {buildNumber}");
        }

        static string GetRegistryValue(string path, string valueName)
        {
            using (var key = Registry.LocalMachine.OpenSubKey(path))
            {
                if (key != null)
                {
                    object value = key.GetValue(valueName);
                    return value?.ToString() ?? "Nie znaleziono wartości";
                }
            }
            return "Nie znaleziono klucza";
        }
    }
}