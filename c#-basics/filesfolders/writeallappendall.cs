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
            string filePath = Path.Combine(cwd, "WriteLines2.txt");

            if (!File.Exists(filePath))
            {
                string createText = "Hello and Welcome" + Environment.NewLine;
                File.WriteAllText(filePath, createText);
            } else
            {
                string appendText = "File already exists, so we append that line" + Environment.NewLine;
                File.AppendAllText(filePath, appendText);
            }
        }
    }
}
