using System;
using System.IO;
using System.Net;

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

            string status = isOnline ? "dostępna" : "niedostępna";
            Console.WriteLine($"Strona {status}!");

            LogResult(url, status);
        }
    }

    static string NormalizeUrl(string input)
    {
        if (!input.StartsWith("http://") && !input.StartsWith("https://"))
        {
            input = "http://" + input; // Domyślnie dodajemy http
        }
        return input;
    }

    static bool IsValidUrl(string url)
    {
        return Uri.TryCreate(url, UriKind.Absolute, out Uri uriResult)
               && (uriResult.Scheme == Uri.UriSchemeHttp || uriResult.Scheme == Uri.UriSchemeHttps);
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

    static void LogResult(string url, string status)
    {
        string logMessage = $"[{DateTime.Now:yyyy-MM-dd HH:mm:ss}] Sprawdzono adres: {url}. Strona {status}.";
        File.AppendAllText("log.txt", logMessage + Environment.NewLine);
    }
}
