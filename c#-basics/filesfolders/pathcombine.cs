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
            string directory = "somefolder";

            if (Directory.Exists(Path.Combine(basePath, directory)))
            {
                Console.WriteLine("Directory exists!");
            }
        }
    }
}
