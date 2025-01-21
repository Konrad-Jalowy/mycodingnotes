using System;

using System.Collections.Generic;
using Microsoft.Win32;

namespace ListaZainstalowanychProgramow
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> programy = GetInstalledPrograms();

            Console.WriteLine("Zainstalowane programy:");
            Console.WriteLine("-----------------------");

            foreach (var program in programy)
            {
                Console.WriteLine(program);
            }

            Console.WriteLine("-----------------------");
            Console.WriteLine($"Łączna liczba programów: {programy.Count}");
            Console.WriteLine("Naciśnij dowolny klawisz, aby zakończyć...");
            Console.ReadKey();
        }

        /// <summary>
        /// Pobiera listę zainstalowanych programów z rejestru.
        /// </summary>
        /// <returns>Lista nazw programów.</returns>
        static List<string> GetInstalledPrograms()
        {
            List<string> programs = new List<string>();

            // Lokalizacje rejestru, gdzie mogą być zapisane informacje o programach
            string[] registryKeys = new string[]
            {
                @"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                @"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall" // Dla 32-bitowych programów na 64-bitowym Windows
            };

            foreach (string keyPath in registryKeys)
            {
                using (RegistryKey key = Registry.LocalMachine.OpenSubKey(keyPath))
                {
                    if (key == null)
                        continue;

                    foreach (string subkeyName in key.GetSubKeyNames())
                    {
                        using (RegistryKey subkey = key.OpenSubKey(subkeyName))
                        {
                            if (subkey == null)
                                continue;

                            // Pobranie nazwy programu
                            object displayName = subkey.GetValue("DisplayName");
                            if (displayName != null)
                            {
                                string name = displayName.ToString();
                                if (!programs.Contains(name))
                                {
                                    programs.Add(name);
                                }
                            }
                        }
                    }
                }
            }

            // Opcjonalnie: Dodatkowo sprawdzenie dla bieżącego użytkownika
            string userUninstallKey = @"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall";
            using (RegistryKey key = Registry.CurrentUser.OpenSubKey(userUninstallKey))
            {
                if (key != null)
                {
                    foreach (string subkeyName in key.GetSubKeyNames())
                    {
                        using (RegistryKey subkey = key.OpenSubKey(subkeyName))
                        {
                            if (subkey == null)
                                continue;

                            object displayName = subkey.GetValue("DisplayName");
                            if (displayName != null)
                            {
                                string name = displayName.ToString();
                                if (!programs.Contains(name))
                                {
                                    programs.Add(name);
                                }
                            }
                        }
                    }
                }
            }

            return programs;
        }
    }
}
