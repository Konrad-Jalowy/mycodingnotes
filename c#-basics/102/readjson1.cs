using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
namespace ConsoleApp13
{
    class Program
    {
        static void Main(string[] args)
        {
           
            string fileName = @"C:\csharpoutput\somefile.json";
            using (StreamReader sr = new StreamReader(fileName))
            {
                string json = sr.ReadToEnd();
                var config = JsonSerializer.Deserialize<Dictionary<string, string>>(json);
                Console.WriteLine(config["name"]); //John Doe
                Console.WriteLine(config["age"]); //25
            }                          
        }
    }
}
