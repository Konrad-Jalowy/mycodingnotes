using System;
using System.Net;
using System.Net.NetworkInformation;
using System.Net.Sockets;
using System.Linq;

class Program
{
    static void Main()
    {
        foreach (NetworkInterface nic in NetworkInterface.GetAllNetworkInterfaces())
        {
            if (nic.OperationalStatus == OperationalStatus.Up)
            {
                var ipProps = nic.GetIPProperties();
                var ipAddress = ipProps.UnicastAddresses
                    .Where(ip => ip.Address.AddressFamily == AddressFamily.InterNetwork)
                    .Select(ip => ip.Address.ToString())
                    .FirstOrDefault();

                if (!string.IsNullOrEmpty(ipAddress))
                {
                    Console.WriteLine($"[TESTUJEMY INTERFEJS] {nic.Name} ({nic.NetworkInterfaceType})");
                    Console.WriteLine($"Adres IP: {ipAddress}");
                    Console.WriteLine($"Próba połączenia z Google...");

                    if (CanConnectToGoogle(ipAddress))
                    {
                        Console.WriteLine($"✅ INTERFEJS {nic.Name} MA POŁĄCZENIE Z INTERNETEM!");
                    }
                    else
                    {
                        Console.WriteLine($"❌ INTERFEJS {nic.Name} NIE MA POŁĄCZENIA.");
                    }

                    Console.WriteLine(new string('-', 40));
                }
            }
        }
    }

    static bool CanConnectToGoogle(string localIp)
    {
        try
        {
            var client = new TcpClient();
            var endpoint = new IPEndPoint(IPAddress.Parse(localIp), 0);
            client.Client.Bind(endpoint); // Wymuszenie użycia konkretnego interfejsu
            client.Connect("google.com", 80); // Połączenie na port HTTP (80)
            return true;
        }
        catch
        {
            return false;
        }
    }
}
