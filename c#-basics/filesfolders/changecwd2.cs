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
            Directory.SetCurrentDirectory(target);
            Console.WriteLine(Directory.GetCurrentDirectory());
        }
    }
}