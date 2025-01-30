using System;
using System.Linq;
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

                if (!string.IsNullOrEmpty(ipAddress))
                {
                    Console.WriteLine($"[POŁĄCZONY Z SIECIĄ] {nic.Name} ({nic.NetworkInterfaceType})");
                    Console.WriteLine($"Adres MAC: {nic.GetPhysicalAddress()}");
                    Console.WriteLine($"Adres IP: {ipAddress}");
                    Console.WriteLine(new string('-', 40));
                }
                else
                {
                    Console.WriteLine($"[NIE MA INTERNETU] {nic.Name} ({nic.NetworkInterfaceType})");
                }
            }
        }
    }
}

