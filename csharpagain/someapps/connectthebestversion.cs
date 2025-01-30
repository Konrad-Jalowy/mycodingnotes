using System;
using System.Linq;
using System.Net;
using System.Net.NetworkInformation;
using System.Net.Sockets;

class Program
{
    static void Main()
    {
        foreach (NetworkInterface nic in NetworkInterface.GetAllNetworkInterfaces())
        {
            if ((nic.NetworkInterfaceType == NetworkInterfaceType.Ethernet ||
                nic.NetworkInterfaceType == NetworkInterfaceType.Wireless80211) &&
                nic.OperationalStatus == OperationalStatus.Up)
            {
                var ipProps = nic.GetIPProperties();
                var ipAddress = ipProps.UnicastAddresses
                    .Where(ip => ip.Address.AddressFamily == AddressFamily.InterNetwork)
                    .Select(ip => ip.Address.ToString())
                    .FirstOrDefault();

                var gateway = ipProps.GatewayAddresses
                    .Select(gw => gw.Address.ToString())
                    .FirstOrDefault();

                Console.WriteLine($"[SPRAWDZAMY INTERFEJS] {nic.Name} ({nic.NetworkInterfaceType})");
                Console.WriteLine($"Adres IP: {ipAddress}");
                Console.WriteLine($"Bramka domyślna (Gateway): {gateway ?? "Brak"}");

                if (string.IsNullOrEmpty(gateway))
                {
                    Console.WriteLine($"❌ {nic.Name} nie ma bramy domyślnej – NIE MA INTERNETU.");
                }
                else if (CanConnectToGoogle(ipAddress))
                {
                    Console.WriteLine($"✅ {nic.Name} rzeczywiście łączy się z Internetem!");
                }
                else
                {
                    Console.WriteLine($"❌ {nic.Name} nie może wysyłać ruchu do Internetu.");
                }

                Console.WriteLine(new string('-', 40));
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
