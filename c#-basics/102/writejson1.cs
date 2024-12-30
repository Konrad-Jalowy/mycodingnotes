using System;
using System.IO;
using System.Text.Json;
namespace ConsoleApp13
{
    class Program
    {
        static void Main(string[] args)
        {
           
            string fileName = @"C:\csharpoutput\somefile.json";
            string jsonString = JsonSerializer.Serialize(new
            {
                name = "John Doe",
                age = 25
            }
            );

            File.WriteAllText(fileName, jsonString);

            Console.WriteLine(File.ReadAllText(fileName));
        }
    }
}
