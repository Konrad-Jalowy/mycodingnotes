using System;

namespace ConsoleApp20
{
    delegate void Logger(string message);

    class Program
    {
        static void Main()
        {
            Logger logger = Console.WriteLine;

            ProcessData("Hello, World!", logger);
        }

        static void ProcessData(string data, Logger log)
        {
            log($"Przetwarzanie danych: {data}");
        }
    }
}
