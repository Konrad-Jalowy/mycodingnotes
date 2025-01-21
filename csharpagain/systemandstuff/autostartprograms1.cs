namespace ConsoleApp20
{
    using System;
    using Microsoft.Win32;

    class Program
    {
        static void Main()
        {
            string userRunKey = @"Software\Microsoft\Windows\CurrentVersion\Run";
            string machineRunKey = @"SOFTWARE\Microsoft\Windows\CurrentVersion\Run";

            Console.WriteLine("Programy w autostarcie (bieżący użytkownik):");
            DisplayStartupPrograms(userRunKey, Registry.CurrentUser);

            Console.WriteLine("\nProgramy w autostarcie (wszyscy użytkownicy):");
            DisplayStartupPrograms(machineRunKey, Registry.LocalMachine);
        }

        static void DisplayStartupPrograms(string path, RegistryKey baseKey)
        {
            using (var key = baseKey.OpenSubKey(path))
            {
                if (key != null)
                {
                    foreach (var valueName in key.GetValueNames())
                    {
                        Console.WriteLine($"{valueName}: {key.GetValue(valueName)}");
                    }
                }
                else
                {
                    Console.WriteLine("Brak programów w autostarcie.");
                }
            }
        }
    }

}