using System;

namespace ConsoleApp20
{
    using System;
    using Microsoft.Win32;

    class Program
    {
        static void Main()
        {
            string registryPath = @"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced";

            using (var key = Registry.CurrentUser.OpenSubKey(registryPath))
            {
                if (key != null)
                {
                    object hiddenValue = key.GetValue("Hidden");
                    Console.WriteLine($"Wartość 'Hidden': {hiddenValue}");
                }
                else
                {
                    Console.WriteLine("Klucz rejestru nie istnieje.");
                }
            }
        }
    }


}