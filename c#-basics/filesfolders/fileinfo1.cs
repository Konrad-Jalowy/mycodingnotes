using System;
using System.IO;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Starting App!");

            string target = @"C:\csharpoutput";

            Directory.SetCurrentDirectory(target);

            string cwd = Directory.GetCurrentDirectory();
            string filePath = Path.Combine(cwd, "WriteLines3.txt");

            FileInfo myfile = new FileInfo(filePath);
            if (!myfile.Exists)
            {
                Console.WriteLine($"File {myfile.FullName} doesnt exist!");
            }
        }
    }
}