using System;
using System.Net.NetworkInformation;

class Program
{
    static void Main()
    {
        foreach (NetworkInterface nic in NetworkInterface.GetAllNetworkInterfaces())
        {
            if ((nic.NetworkInterfaceType == NetworkInterfaceType.Ethernet ||
                nic.NetworkInterfaceType == NetworkInterfaceType.Wireless80211) &&
                nic.OperationalStatus == OperationalStatus.Up) // Sprawdzamy aktywne
            {
                Console.WriteLine($"[AKTYWNE] {nic.Name} ({nic.NetworkInterfaceType})");
                Console.WriteLine($"Adres MAC: {nic.GetPhysicalAddress()}");
                Console.WriteLine(new string('-', 40));
            }
        }
    }
}