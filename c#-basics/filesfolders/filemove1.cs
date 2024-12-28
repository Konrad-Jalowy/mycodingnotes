using System;
using System.IO;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string sourcePath = Path.Combine(cwd, "WriteLinesCopy.txt");
         
            bool sourceExists = File.Exists(sourcePath);
            bool copiesExists = Directory.Exists(Path.Combine(cwd, "copies"));
            
            if (sourceExists && copiesExists)
            {
                string destPath = Path.Combine(cwd, "copies", "WriteLinesCopy.txt");
                File.Move(sourcePath, destPath);
            }            
        }
    }
}