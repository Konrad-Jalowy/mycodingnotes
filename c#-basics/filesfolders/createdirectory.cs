using System;
using System.IO;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string basePath = Directory.GetCurrentDirectory();
            string directory = @"somefolder2";
            string path = Path.Combine(basePath, directory);
            Console.WriteLine(path);

            if (!Directory.Exists(path))
            {
                Console.WriteLine("Creating directory!");
                Directory.CreateDirectory(path);
            }
        }
    }
}