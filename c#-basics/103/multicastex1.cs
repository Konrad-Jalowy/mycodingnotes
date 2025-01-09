namespace ConsoleApp18
{
    public delegate void LogDelegate(string message);

    class Program
    {
        static void LogToFile(string message)
        {
            Console.WriteLine($"[FILE]: {message}");
        }

        static void LogToConsole(string message)
        {
            Console.WriteLine($"[CONSOLE]: {message}");
        }

        static void LogToSystem(string message)
        {
            Console.WriteLine($"[SYSTEM]: {message}");
        }

        static void Main()
        {
            LogDelegate log = LogToFile;
            log += LogToConsole;
            log += LogToSystem;

            log("This is a log message.");
        }
    }
}