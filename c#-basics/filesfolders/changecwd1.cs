using System;
using System.IO;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string target = @"C:\somepath";
            if (!Directory.Exists(target))
            {
                Directory.CreateDirectory(target);
            }
            Environment.CurrentDirectory = (target);
            Console.WriteLine(Directory.GetCurrentDirectory());
        }
    }
}