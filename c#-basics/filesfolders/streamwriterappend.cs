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
            string[] lines = { "First line", "Second line", "Third line" };

            using (StreamWriter outputFile = new StreamWriter(Path.Combine(cwd, "WriteLines.txt"), append: true))
            {
                foreach (string line in lines)
                    outputFile.WriteLine(line);
            }
        }
    
    }
}
