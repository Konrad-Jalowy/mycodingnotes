using System;
using System.Net;
using System.Text.RegularExpressions;

class Program
{
    static void Main()
    {
        while (true)
        {
            Console.Write("Podaj adres URL (lub wpisz 'exit' aby wyjść): ");
            string input = Console.ReadLine().Trim();

            if (input.Equals("exit", StringComparison.OrdinalIgnoreCase))
            {
                Console.WriteLine("Zamykanie programu...");
                break;
            }

            string url = NormalizeUrl(input);

            if (!IsValidUrl(url))
            {
                Console.WriteLine("Błędny adres URL. Spróbuj ponownie.");
                continue;
            }

            Console.WriteLine($"Sprawdzam dostępność strony: {url}");
            bool isOnline = IsWebsiteOnline(url);

            Console.WriteLine(isOnline ? "Strona jest online!" : "Strona jest offline lub niedostępna.");
        }
    }

    static string NormalizeUrl(string input)
    {
        if (!input.StartsWith("http://") && !input.StartsWith("https://"))
        {
            return "http://" + input; // Domyślnie dodajemy http
        }
        return input;
    }

    static bool IsValidUrl(string url)
    {
        string pattern = @"^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([\/\w .-]*)*\/?$";
        return Regex.IsMatch(url, pattern);
    }

    static bool IsWebsiteOnline(string url)
    {
        try
        {
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.Method = "HEAD";
            request.Timeout = 5000; // 5 sekund na odpowiedź
            using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())
            {
                return response.StatusCode == HttpStatusCode.OK;
            }
        }
        catch
        {
            return false;
        }
    }
}
