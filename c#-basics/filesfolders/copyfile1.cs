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
            string sourcePath = Path.Combine(cwd, "WriteLines.txt");
            string destPath = Path.Combine(cwd, "WriteLinesCopy.txt");

            bool sourceExists = File.Exists(sourcePath);
            bool destExists = File.Exists(destPath);

            if (sourceExists)
            {
                if (!destExists)
                {
                    File.Copy(sourcePath, destPath);
                }
            }
        }
    }
}
