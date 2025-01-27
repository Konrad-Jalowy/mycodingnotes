using System;
using System.IO;
using System.Collections.Generic;

class FileSystemApp
{
    static void Main()
    {
        string currentDirectory = Directory.GetCurrentDirectory();

        Console.WriteLine("Witaj w prostym systemie plików!");
        Console.WriteLine("Dostępne komendy: ls, cd, mkdir, rmdir, create, delete, read, write, help, exit\n");

        while (true)
        {
            Console.Write($"{currentDirectory}> ");
            string command = Console.ReadLine();

            if (string.IsNullOrWhiteSpace(command))
                continue;

            var (action, argument, flags) = ParseCommand(command);

            switch (action)
            {
                case "ls":
                    ListDirectory(currentDirectory, argument, flags);
                    break;
                case "cd":
                    ChangeDirectory(ref currentDirectory, argument);
                    break;
                case "mkdir":
                    CreateDirectory(currentDirectory, argument);
                    break;
                case "rmdir":
                    RemoveDirectory(currentDirectory, argument);
                    break;
                case "create":
                    CreateFile(currentDirectory, argument);
                    break;
                case "delete":
                    DeleteFile(currentDirectory, argument);
                    break;
                case "read":
                    ReadFile(currentDirectory, argument, flags);
                    break;
                case "write":
                    WriteToFile(currentDirectory, argument, flags);
                    break;
                case "help":
                    ShowHelp();
                    break;
                case "exit":
                    Console.WriteLine("Do zobaczenia!");
                    return;
                default:
                    Console.WriteLine("Nieznana komenda. Wpisz 'help', aby zobaczyć dostępne komendy.");
                    break;
            }
        }
    }

    static (string command, string argument, List<string> flags) ParseCommand(string input)
    {
        var parts = input.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        string command = parts.Length > 0 ? parts[0] : null;
        string argument = null;
        var flags = new List<string>();

        for (int i = 1; i < parts.Length; i++)
        {
            if (parts[i].StartsWith("-"))
            {
                flags.Add(parts[i]);
            }
            else
            {
                argument = parts[i];
            }
        }

        return (command, argument, flags);
    }

    static void ListDirectory(string directory, string subDirectory, List<string> flags)
    {
        string targetDirectory = subDirectory == null ? directory : Path.Combine(directory, subDirectory);

        if (subDirectory != null && !Directory.Exists(targetDirectory))
        {
            Console.WriteLine($"Katalog '{subDirectory}' nie istnieje lub nie jest katalogiem.");
            return;
        }

        Console.WriteLine("\nZawartość katalogu:");
        Console.WriteLine("Foldery:");
        foreach (var dir in Directory.GetDirectories(targetDirectory))
        {
            Console.WriteLine($"- {Path.GetFileName(dir)}");
        }

        Console.WriteLine("\nPliki:");
        foreach (var file in Directory.GetFiles(targetDirectory))
        {
            var fileInfo = new FileInfo(file);
            if (flags.Contains("-a"))
            {
                Console.WriteLine($"- {Path.GetFileName(file)} ({fileInfo.Length} bajtów)");
            }
            else
            {
                Console.WriteLine($"- {Path.GetFileName(file)}");
            }
        }
        Console.WriteLine();
    }

    static void ChangeDirectory(ref string currentDirectory, string newDir)
    {
        if (string.IsNullOrWhiteSpace(newDir))
        {
            Console.WriteLine("Podaj nazwę katalogu.");
            return;
        }

        string targetDirectory = Path.IsPathRooted(newDir) ? newDir : Path.Combine(currentDirectory, newDir);

        try
        {
            string normalizedPath = Path.GetFullPath(targetDirectory);
            if (Directory.Exists(normalizedPath))
            {
                currentDirectory = normalizedPath;
            }
            else
            {
                Console.WriteLine($"Katalog '{newDir}' nie istnieje.");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Błąd zmiany katalogu: {ex.Message}");
        }
    }

    static void CreateDirectory(string currentDirectory, string dirName)
    {
        if (string.IsNullOrWhiteSpace(dirName))
        {
            Console.WriteLine("Podaj nazwę katalogu do utworzenia.");
            return;
        }

        string newDirectory = Path.Combine(currentDirectory, dirName);
        if (!Directory.Exists(newDirectory))
        {
            Directory.CreateDirectory(newDirectory);
            Console.WriteLine($"Katalog '{dirName}' został utworzony.");
        }
        else
        {
            Console.WriteLine($"Katalog '{dirName}' już istnieje.");
        }
    }

    static void RemoveDirectory(string currentDirectory, string dirName)
    {
        if (string.IsNullOrWhiteSpace(dirName))
        {
            Console.WriteLine("Podaj nazwę katalogu do usunięcia.");
            return;
        }

        string directoryToRemove = Path.Combine(currentDirectory, dirName);
        if (Directory.Exists(directoryToRemove))
        {
            try
            {
                Directory.Delete(directoryToRemove);
                Console.WriteLine($"Katalog '{dirName}' został usunięty.");
            }
            catch (IOException)
            {
                Console.WriteLine("Katalog nie jest pusty i nie może zostać usunięty.");
            }
        }
        else
        {
            Console.WriteLine($"Katalog '{dirName}' nie istnieje.");
        }
    }

    static void CreateFile(string currentDirectory, string fileName)
    {
        if (string.IsNullOrWhiteSpace(fileName))
        {
            Console.WriteLine("Podaj nazwę pliku do utworzenia.");
            return;
        }

        string newFile = Path.Combine(currentDirectory, fileName);
        if (!File.Exists(newFile))
        {
            File.Create(newFile).Close();
            Console.WriteLine($"Plik '{fileName}' został utworzony.");
        }
        else
        {
            Console.WriteLine($"Plik '{fileName}' już istnieje.");
        }
    }

    static void DeleteFile(string currentDirectory, string fileName)
    {
        if (string.IsNullOrWhiteSpace(fileName))
        {
            Console.WriteLine("Podaj nazwę pliku do usunięcia.");
            return;
        }

        string fileToDelete = Path.Combine(currentDirectory, fileName);
        if (File.Exists(fileToDelete))
        {
            File.Delete(fileToDelete);
            Console.WriteLine($"Plik '{fileName}' został usunięty.");
        }
        else
        {
            Console.WriteLine($"Plik '{fileName}' nie istnieje.");
        }
    }

    static void ReadFile(string currentDirectory, string fileName, List<string> flags)
    {
        if (string.IsNullOrWhiteSpace(fileName))
        {
            Console.WriteLine("Podaj nazwę pliku do odczytu.");
            return;
        }

        string fileToRead = Path.Combine(currentDirectory, fileName);
        if (File.Exists(fileToRead))
        {
            try
            {
                string[] lines = File.ReadAllLines(fileToRead);
                if (lines.Length == 0)
                {
                    Console.WriteLine($"Plik '{fileName}' jest pusty.");
                }
                else
                {
                    Console.WriteLine($"\nZawartość pliku '{fileName}':");
                    for (int i = 0; i < lines.Length; i++)
                    {
                        if (flags.Contains("-l"))
                        {
                            Console.WriteLine($"{i + 1}: {lines[i]}");
                        }
                        else
                        {
                            Console.WriteLine(lines[i]);
                        }
                    }
                    Console.WriteLine();
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Błąd odczytu pliku: {ex.Message}");
            }
        }
        else
        {
            Console.WriteLine($"Plik '{fileName}' nie istnieje.");
        }
    }

    static void WriteToFile(string currentDirectory, string fileName, List<string> flags)
    {
        if (string.IsNullOrWhiteSpace(fileName))
        {
            Console.WriteLine("Podaj nazwę pliku do zapisu.");
            return;
        }

        string fileToWrite = Path.Combine(currentDirectory, fileName);
        if (File.Exists(fileToWrite))
        {
            bool append = !flags.Contains("-w");
            Console.WriteLine("Wprowadź dane do zapisania (zakończ wprowadzanie wpisując '\\0' w nowej linii):");

            using (StreamWriter writer = new StreamWriter(fileToWrite, append))
            {
                while (true)
                {
                    string line = Console.ReadLine();
                    if (line == "\\0") break;
                    writer.WriteLine(line);
                }
            }

            Console.WriteLine($"Dane zostały zapisane do pliku '{fileName}'.");
        }
        else
        {
            Console.WriteLine($"Plik '{fileName}' nie istnieje.");
        }
    }

    static void ShowHelp()
    {
        Console.WriteLine("\nDostępne komendy:");
        Console.WriteLine("ls - Wyświetl zawartość bieżącego katalogu");
        Console.WriteLine("ls [nazwa katalogu] - Wyświetl zawartość podkatalogu");
        Console.WriteLine("ls -a - Wyświetl dodatkowe informacje o plikach");
        Console.WriteLine("cd [nazwa] - Przejdź do innego katalogu");
        Console.WriteLine("mkdir [nazwa] - Utwórz nowy katalog");
        Console.WriteLine("rmdir [nazwa] - Usuń pusty katalog");
        Console.WriteLine("create [nazwa] - Utwórz nowy plik");
        Console.WriteLine("delete [nazwa] - Usuń plik");
        Console.WriteLine("read [nazwa] - Odczytaj zawartość pliku");
        Console.WriteLine("read -l [nazwa] - Odczytaj zawartość pliku z numerami linii");
        Console.WriteLine("write [nazwa] - Dopisz dane do pliku");
        Console.WriteLine("write -w [nazwa] - Nadpisz dane w pliku");
        Console.WriteLine("help - Wyświetl pomoc");
        Console.WriteLine("exit - Zakończ program\n");
    }
}
