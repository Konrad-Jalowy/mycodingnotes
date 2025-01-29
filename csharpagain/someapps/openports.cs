using System;
using System.Linq;
using System.Net.NetworkInformation;

class Program
{
    static void Main()
    {
        Console.WriteLine("Lista otwartych portów:");
        ShowOpenPorts();
        Console.WriteLine("\nNaciśnij dowolny klawisz, aby zakończyć...");
        Console.ReadKey();
    }

    static void ShowOpenPorts()
    {
        var activeConnections = IPGlobalProperties.GetIPGlobalProperties().GetActiveTcpListeners();

        if (activeConnections.Length == 0)
        {
            Console.WriteLine("Brak otwartych portów.");
            return;
        }

        foreach (var endpoint in activeConnections.OrderBy(e => e.Port))
        {
            Console.WriteLine($"Port: {endpoint.Port} | Adres: {endpoint.Address}");
        }
    }
}
