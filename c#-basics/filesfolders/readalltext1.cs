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
            string filePath = Path.Combine(cwd, "WriteLines.txt");

            if (File.Exists(filePath))
            {
                string text = File.ReadAllText(filePath);
                Console.Write(text);
            }
                  
        }
    }
}