using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            string time = "   09";
            Console.WriteLine(time.TrimStart(new char[] { '0', ' ' }));
        }
    }
}
