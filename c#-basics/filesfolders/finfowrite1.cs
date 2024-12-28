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
            string filePath = Path.Combine(cwd, "WriteLines4.txt");

            FileInfo myfile = new FileInfo(filePath);
            if (!myfile.Exists)
            {
             using (StreamWriter sw = myfile.CreateText())
                 {
                    sw.WriteLine("Hello");
                    sw.WriteLine("And");
                    sw.WriteLine("Welcome");
                 } 
            } 
        }
    }
}
