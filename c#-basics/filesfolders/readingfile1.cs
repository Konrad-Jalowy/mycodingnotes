using System;
using System.IO;
using System.Text;
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
            string path = Path.Combine(cwd, "WriteLines.txt");

            if (File.Exists(path))
            {
                using (FileStream fs = File.OpenRead(path))
                {
                    byte[] b = new byte[1024];
                    UTF8Encoding temp = new UTF8Encoding(true);
                    int readLen;
                    while ((readLen = fs.Read(b, 0, b.Length)) > 0)
                    {
                        Console.WriteLine(temp.GetString(b, 0, readLen));
                    }
                }
            }
           

        }
    
    }
}
