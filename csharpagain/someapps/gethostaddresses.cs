using System;
using System.Net;

class Program
{
    static void Main()
    {
        string hostname = "example.com";
        IPAddress[] addresses = Dns.GetHostAddresses(hostname);

        foreach (var ip in addresses)
        {
            Console.WriteLine(ip);
        }
    }
}
