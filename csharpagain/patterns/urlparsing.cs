namespace ConsoleApp20
{
    class Program
    {
        static void Main()
        {
            string url = "/products?id=123";

            string result = url switch
            {
                "/home" => "Strona główna",
                "/about" => "O nas",
                var s when s.StartsWith("/products") => "Lista produktów",
                _ => "Nieznany URL"
            };

            Console.WriteLine(result);
        }
    }
}