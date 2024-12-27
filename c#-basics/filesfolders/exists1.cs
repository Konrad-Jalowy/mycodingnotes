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
            string path = Path.Combine(cwd, "WriteLines.txt");

            if (File.Exists(path))
            {
                Console.WriteLine($"Working directory: {cwd}");
                Console.WriteLine($"File {Path.GetFileName(path)} exists!");
            }
        }
    
    }
}