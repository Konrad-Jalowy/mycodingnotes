using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        using HttpClient client = new HttpClient();
        string response = await client.GetStringAsync("https://example.com");
        Console.WriteLine(response);
    }
}
