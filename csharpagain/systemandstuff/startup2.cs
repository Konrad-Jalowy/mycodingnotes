namespace ConsoleApp20
{
    using System;
    using System.IO;

    class Program
    {
        static void Main()
        {
            ShowStartupFolder("Folder użytkownika:", Environment.SpecialFolder.Startup);
            ShowStartupFolder("Folder wspólny dla wszystkich użytkowników:", Environment.SpecialFolder.CommonStartup);

            Console.WriteLine("\nNaciśnij Enter, aby zakończyć...");
            Console.ReadLine();
        }

        static void ShowStartupFolder(string title, Environment.SpecialFolder specialFolder)
        {
            string folderPath = Environment.GetFolderPath(specialFolder);

            Console.WriteLine($"\n{title} {folderPath}");
            if (Directory.Exists(folderPath))
            {
                string[] files = Directory.GetFiles(folderPath);
                if (files.Length == 0)
                {
                    Console.WriteLine("Brak plików w tym folderze.");
                }
                else
                {
                    foreach (var file in files)
                    {
                        Console.WriteLine(Path.GetFileName(file));
                    }
                }
            }
            else
            {
                Console.WriteLine("Folder nie istnieje.");
            }
        }
    }
}