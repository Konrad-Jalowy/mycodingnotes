namespace ConsoleApp20
{
 
    public class Log
    {
        public string Level { get; set; }
        public string Message { get; set; }
    }

    class Program
    {
        static void Main()
        {
            Log log = new Log { Level = "ERROR", Message = "Błąd połączenia z bazą danych." };

            string result = log switch
            {
                { Level: "INFO" } => $"Informacja: {log.Message}",
                { Level: "WARNING" } => $"Ostrzeżenie: {log.Message}",
                { Level: "ERROR" } => $"Błąd krytyczny: {log.Message}",
                _ => "Nieznany poziom logu"
            };

            Console.WriteLine(result);
        }
    }

}