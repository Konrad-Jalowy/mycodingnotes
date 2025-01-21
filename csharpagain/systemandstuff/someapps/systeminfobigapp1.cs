using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Microsoft.Win32;
using System.Management;
using System.Net.NetworkInformation;
using System.Net;

namespace SystemInfoApp
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                Console.Clear();
                Console.WriteLine("=== System Info CLI Application ===");
                Console.WriteLine("1. Wyświetl zainstalowane programy");
                Console.WriteLine("2. Sprawdź status ukrytych plików/folderów");
                Console.WriteLine("3. Sprawdź widoczność rozszerzeń plików");
                Console.WriteLine("4. Informacje o dyskach");
                Console.WriteLine("5. Inne informacje systemowe");
                Console.WriteLine("6. Informacje o procesorze");
                Console.WriteLine("7. Informacje o pamięci RAM");
                Console.WriteLine("8. Informacje o sieci");
                Console.WriteLine("9. Informacje o urządzeniach periferyjnych");
                Console.WriteLine("10. Wyjście");
                Console.Write("Wybierz opcję (1-10): ");

                string choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        ListInstalledPrograms();
                        break;
                    case "2":
                        CheckHiddenFilesStatus();
                        break;
                    case "3":
                        CheckFileExtensionsVisibility();
                        break;
                    case "4":
                        DisplayDiskInfo();
                        break;
                    case "5":
                        DisplaySystemInfo();
                        break;
                    case "6":
                        DisplayProcessorInfo();
                        break;
                    case "7":
                        DisplayMemoryInfo();
                        break;
                    case "8":
                        DisplayNetworkInfo();
                        break;
                    case "9":
                        DisplayPeripheralDevices();
                        break;
                    case "10":
                        Console.WriteLine("Zakończono działanie aplikacji. Naciśnij dowolny klawisz...");
                        Console.ReadKey();
                        return;
                    default:
                        Console.WriteLine("Nieprawidłowy wybór. Naciśnij dowolny klawisz, aby spróbować ponownie.");
                        Console.ReadKey();
                        break;
                }
            }
        }

        /// <summary>
        /// Wyświetla listę zainstalowanych programów z rejestru.
        /// </summary>
        static void ListInstalledPrograms()
        {
            Console.Clear();
            Console.WriteLine("=== Zainstalowane Programy ===\n");

            List<string> programs = new List<string>();

            // Klucze rejestru dla zainstalowanych programów
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

            if (programs.Count == 0)
            {
                Console.WriteLine("Nie znaleziono zainstalowanych programów.");
            }
            else
            {
                foreach (var program in programs.OrderBy(p => p))
                {
                    Console.WriteLine(program);
                }
                Console.WriteLine($"\nŁączna liczba programów: {programs.Count}");
            }

            Console.WriteLine("\nNaciśnij dowolny klawisz, aby wrócić do menu głównego...");
            Console.ReadKey();
        }

        /// <summary>
        /// Sprawdza, czy system pokazuje ukryte pliki i foldery.
        /// </summary>
        static void CheckHiddenFilesStatus()
        {
            Console.Clear();
            Console.WriteLine("=== Status Ukrytych Plików/Foldrów ===\n");

            try
            {
                using (RegistryKey key = Registry.CurrentUser.OpenSubKey(@"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"))
                {
                    if (key != null)
                    {
                        object hidden = key.GetValue("Hidden");
                        object hideFileExt = key.GetValue("HideFileExt");

                        if (hidden != null)
                        {
                            // Wartość "Hidden": 1 = Pokaż ukryte pliki, 2 = Ukryj ukryte pliki
                            bool showHidden = ((int)hidden) == 1;
                            Console.WriteLine($"Ukryte pliki i foldery są {(showHidden ? "pokazywane" : "niewidoczne")}");
                        }
                        else
                        {
                            Console.WriteLine("Nie znaleziono ustawienia ukrytych plików/foldrów.");
                        }

                        if (hideFileExt != null)
                        {
                            // Wartość "HideFileExt": 0 = Pokaż rozszerzenia, 1 = Ukryj rozszerzenia
                            bool showFileExt = ((int)hideFileExt) == 0;
                            Console.WriteLine($"Rozszerzenia plików są {(showFileExt ? "widoczne" : "ukryte")}");
                        }
                        else
                        {
                            Console.WriteLine("Nie znaleziono ustawienia widoczności rozszerzeń plików.");
                        }
                    }
                    else
                    {
                        Console.WriteLine("Nie można otworzyć klucza rejestru.");
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Wystąpił błąd podczas odczytu rejestru: {ex.Message}");
            }

            Console.WriteLine("\nNaciśnij dowolny klawisz, aby wrócić do menu głównego...");
            Console.ReadKey();
        }

        /// <summary>
        /// Sprawdza, czy rozszerzenia plików są widoczne w systemie.
        /// </summary>
        static void CheckFileExtensionsVisibility()
        {
            Console.Clear();
            Console.WriteLine("=== Widoczność Rozszerzeń Plików ===\n");

            try
            {
                using (RegistryKey key = Registry.CurrentUser.OpenSubKey(@"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"))
                {
                    if (key != null)
                    {
                        object hideFileExt = key.GetValue("HideFileExt");

                        if (hideFileExt != null)
                        {
                            bool showFileExt = ((int)hideFileExt) == 0;
                            Console.WriteLine($"Rozszerzenia plików są {(showFileExt ? "widoczne" : "ukryte")}");
                        }
                        else
                        {
                            Console.WriteLine("Nie znaleziono ustawienia widoczności rozszerzeń plików.");
                        }
                    }
                    else
                    {
                        Console.WriteLine("Nie można otworzyć klucza rejestru.");
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Wystąpił błąd podczas odczytu rejestru: {ex.Message}");
            }

            Console.WriteLine("\nNaciśnij dowolny klawisz, aby wrócić do menu głównego...");
            Console.ReadKey();
        }

        /// <summary>
        /// Wyświetla informacje o dyskach: liczba dysków, typ, pojemność, wolne miejsce.
        /// </summary>
        static void DisplayDiskInfo()
        {
            Console.Clear();
            Console.WriteLine("=== Informacje o Dyskach ===\n");

            DriveInfo[] allDrives = DriveInfo.GetDrives();

            if (allDrives.Length == 0)
            {
                Console.WriteLine("Nie znaleziono dysków w systemie.");
            }
            else
            {
                Console.WriteLine($"Liczba dysków: {allDrives.Length}\n");
                foreach (DriveInfo d in allDrives)
                {
                    Console.WriteLine($"Nazwa: {d.Name}");
                    Console.WriteLine($"  Typ: {d.DriveType}");
                    if (d.IsReady)
                    {
                        Console.WriteLine($"  Format: {d.DriveFormat}");
                        Console.WriteLine($"  Pojemność całkowita: {BytesToGB(d.TotalSize)} GB");
                        Console.WriteLine($"  Wolne miejsce: {BytesToGB(d.TotalFreeSpace)} GB");
                        Console.WriteLine($"  Użyte miejsce: {BytesToGB(d.TotalSize - d.TotalFreeSpace)} GB");
                    }
                    else
                    {
                        Console.WriteLine("  Dysk nie jest gotowy.");
                    }
                    Console.WriteLine();
                }
            }

            Console.WriteLine("Naciśnij dowolny klawisz, aby wrócić do menu głównego...");
            Console.ReadKey();
        }

        /// <summary>
        /// Wyświetla podstawowe informacje systemowe.
        /// </summary>
        static void DisplaySystemInfo()
        {
            Console.Clear();
            Console.WriteLine("=== Inne Informacje Systemowe ===\n");

            try
            {
                Console.WriteLine($"System operacyjny: {Environment.OSVersion}");
                Console.WriteLine($"Wersja .NET: {Environment.Version}");
                Console.WriteLine($"Nazwa komputera: {Environment.MachineName}");
                Console.WriteLine($"Użytkownik: {Environment.UserName}");
                Console.WriteLine($"Architektura systemu: {(Environment.Is64BitOperatingSystem ? "64-bitowy" : "32-bitowy")}");
                Console.WriteLine($"Liczba procesorów: {Environment.ProcessorCount}");
                Console.WriteLine($"Pamięć wirtualna dostępna: {BytesToGB(Environment.WorkingSet)} GB");
                Console.WriteLine($"Ścieżka systemowa: {Environment.GetFolderPath(Environment.SpecialFolder.System)}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Wystąpił błąd podczas pobierania informacji: {ex.Message}");
            }

            Console.WriteLine("\nNaciśnij dowolny klawisz, aby wrócić do menu głównego...");
            Console.ReadKey();
        }

        /// <summary>
        /// Wyświetla informacje o procesorze.
        /// </summary>
        static void DisplayProcessorInfo()
        {
            Console.Clear();
            Console.WriteLine("=== Informacje o Procesorze ===\n");

            try
            {
                using (ManagementObjectSearcher searcher = new ManagementObjectSearcher("select * from Win32_Processor"))
                {
                    foreach (ManagementObject obj in searcher.Get())
                    {
                        Console.WriteLine($"Nazwa: {obj["Name"]}");
                        Console.WriteLine($"Producent: {obj["Manufacturer"]}");
                        Console.WriteLine($"Rodzaj: {obj["ProcessorType"]}");
                        Console.WriteLine($"Liczba rdzeni: {obj["NumberOfCores"]}");
                        Console.WriteLine($"Liczba wątków: {obj["NumberOfLogicalProcessors"]}");
                        Console.WriteLine($"Prędkość (MHz): {obj["MaxClockSpeed"]}");
                        Console.WriteLine();
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Wystąpił błąd podczas pobierania informacji o procesorze: {ex.Message}");
            }

            Console.WriteLine("Naciśnij dowolny klawisz, aby wrócić do menu głównego...");
            Console.ReadKey();
        }

        /// <summary>
        /// Wyświetla informacje o pamięci RAM.
        /// </summary>
        static void DisplayMemoryInfo()
        {
            Console.Clear();
            Console.WriteLine("=== Informacje o Pamięci RAM ===\n");

            try
            {
                using (ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_ComputerSystem"))
                {
                    foreach (ManagementObject obj in searcher.Get())
                    {
                        ulong totalPhysicalMemory = (ulong)obj["TotalPhysicalMemory"];
                        Console.WriteLine($"Całkowita pamięć RAM: {BytesToGB((long)totalPhysicalMemory)} GB");
                        // Aby uzyskać dostęp do dostępnej pamięci RAM, potrzebne jest użycie innego zapytania
                    }
                }

                using (ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_OperatingSystem"))
                {
                    foreach (ManagementObject obj in searcher.Get())
                    {
                        ulong freePhysicalMemory = Convert.ToUInt64(obj["FreePhysicalMemory"]) * 1024; // FreePhysicalMemory is in KB
                        Console.WriteLine($"Dostępna pamięć RAM: {BytesToGB((long)freePhysicalMemory)} GB");
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Wystąpił błąd podczas pobierania informacji o pamięci RAM: {ex.Message}");
            }

            Console.WriteLine("\nNaciśnij dowolny klawisz, aby wrócić do menu głównego...");
            Console.ReadKey();
        }

        /// <summary>
        /// Wyświetla informacje o sieci.
        /// </summary>
        static void DisplayNetworkInfo()
        {
            Console.Clear();
            Console.WriteLine("=== Informacje o Sieci ===\n");

            try
            {
                foreach (NetworkInterface ni in NetworkInterface.GetAllNetworkInterfaces())
                {
                    Console.WriteLine($"Nazwa: {ni.Name}");
                    Console.WriteLine($"  Status: {ni.OperationalStatus}");
                    Console.WriteLine($"  Typ: {ni.NetworkInterfaceType}");
                    Console.WriteLine($"  MAC Address: {ni.GetPhysicalAddress()}");

                    IPInterfaceProperties ipProps = ni.GetIPProperties();
                    foreach (UnicastIPAddressInformation ip in ipProps.UnicastAddresses)
                    {
                        Console.WriteLine($"  Adres IP: {ip.Address}");
                    }

                    Console.WriteLine();
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Wystąpił błąd podczas pobierania informacji o sieci: {ex.Message}");
            }

            Console.WriteLine("Naciśnij dowolny klawisz, aby wrócić do menu głównego...");
            Console.ReadKey();
        }

        /// <summary>
        /// Wyświetla informacje o urządzeniach USB.
        /// </summary>
        static void DisplayPeripheralDevices()
        {
            Console.Clear();
            Console.WriteLine("=== Informacje o Urządzeniach Periferyjnych (USB) ===\n");

            try
            {
                using (ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_USBHub"))
                {
                    foreach (ManagementObject obj in searcher.Get())
                    {
                        Console.WriteLine($"Nazwa: {obj["Name"]}");
                        Console.WriteLine($"  PNP Device ID: {obj["PNPDeviceID"]}");
                        Console.WriteLine($"  Status: {obj["Status"]}");
                        Console.WriteLine();
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Wystąpił błąd podczas pobierania informacji o urządzeniach USB: {ex.Message}");
            }

            Console.WriteLine("Naciśnij dowolny klawisz, aby wrócić do menu głównego...");
            Console.ReadKey();
        }

        /// <summary>
        /// Konwertuje bajty na gigabajty.
        /// </summary>
        /// <param name="bytes">Liczba bajtów</param>
        /// <returns>Gigabajty jako string z dwoma miejscami po przecinku</returns>
        static string BytesToGB(long bytes)
        {
            double gb = bytes / (double)(1024 * 1024 * 1024);
            return gb.ToString("F2");
        }
    }
}
