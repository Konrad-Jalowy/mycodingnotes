using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine($"Current User: {Environment.UserName}");
            string cwd = Environment.CurrentDirectory;
            Console.WriteLine($"CWD: {cwd}");
            Environment.CurrentDirectory = @"C:\csharpoutput";
            Console.WriteLine($"CWD: {Environment.CurrentDirectory}");
        }
    }
}
