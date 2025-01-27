using System;
using System.IO;

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

            string[] parts = command.Split(' ', 2);
            string action = parts[0].ToLower();
            string argument = parts.Length > 1 ? parts[1] : null;

            switch (action)
            {
                case "ls":
                    ListDirectory(currentDirectory);
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
                    ReadFile(currentDirectory, argument);
                    break;
                case "write":
                    WriteToFile(currentDirectory, argument);
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

    static void ListDirectory(string directory)
    {
        Console.WriteLine("\nZawartość katalogu:");
        Console.WriteLine("Foldery:");
        foreach (var dir in Directory.GetDirectories(directory))
        {
            Console.WriteLine($"- {Path.GetFileName(dir)}");
        }

        Console.WriteLine("\nPliki:");
        foreach (var file in Directory.GetFiles(directory))
        {
            Console.WriteLine($"- {Path.GetFileName(file)}");
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

    static void ReadFile(string currentDirectory, string fileName)
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
                string content = File.ReadAllText(fileToRead);
                if (string.IsNullOrEmpty(content))
                {
                    Console.WriteLine($"Plik '{fileName}' jest pusty.");
                }
                else
                {
                    Console.WriteLine($"\nZawartość pliku '{fileName}':\n{content}\n");
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

    static void WriteToFile(string currentDirectory, string fileName)
    {
        if (string.IsNullOrWhiteSpace(fileName))
        {
            Console.WriteLine("Podaj nazwę pliku do zapisu.");
            return;
        }

        string fileToWrite = Path.Combine(currentDirectory, fileName);
        if (File.Exists(fileToWrite))
        {
            Console.WriteLine("Wprowadź dane do zapisania (zakończ wprowadzanie wpisując '\\0' w nowej linii):");

            using (StreamWriter writer = new StreamWriter(fileToWrite, true))
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
        Console.WriteLine("cd [nazwa] - Przejdź do innego katalogu");
        Console.WriteLine("mkdir [nazwa] - Utwórz nowy katalog");
        Console.WriteLine("rmdir [nazwa] - Usuń pusty katalog");
        Console.WriteLine("create [nazwa] - Utwórz nowy plik");
    }
}
