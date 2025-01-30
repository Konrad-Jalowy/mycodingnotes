using System;
using System.Net.NetworkInformation;

class Program
{
    static void Main()
    {
        foreach (NetworkInterface nic in NetworkInterface.GetAllNetworkInterfaces())
        {
            // Sprawdzamy, czy to Ethernet lub WiFi
            if (nic.NetworkInterfaceType == NetworkInterfaceType.Ethernet || 
                nic.NetworkInterfaceType == NetworkInterfaceType.Wireless80211)
            {
                Console.WriteLine($"Nazwa interfejsu: {nic.Name}");
                Console.WriteLine($"Typ interfejsu: {nic.NetworkInterfaceType}");
                Console.WriteLine($"Adres MAC: {nic.GetPhysicalAddress()}");
                Console.WriteLine(new string('-', 40));
            }
        }
    }
}
