namespace Program123
{
    using System;
    using System.Text;

    class DefaultEncoding
    {
        static void Main(string[] args)
        {
            // Pobranie domyślnego kodowania
            Encoding defaultEncoding = Encoding.Default;

            // Wyświetlenie domyślnego kodowania
            Console.WriteLine("Domyślny system kodowania plików: " + defaultEncoding.WebName);

            // Sprawdzenie obsługi Unicode
            bool isUnicode = defaultEncoding.WebName.Contains("utf");
            Console.WriteLine("Czy domyślne kodowanie obsługuje Unicode? " + isUnicode);
        }
    }

}