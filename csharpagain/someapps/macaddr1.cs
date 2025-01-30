using System;
using System.Net.NetworkInformation;

class Program
{
    static void Main()
    {
        foreach (NetworkInterface nic in NetworkInterface.GetAllNetworkInterfaces())
        {
            Console.WriteLine($"Nazwa interfejsu: {nic.Name}");
            Console.WriteLine($"Typ interfejsu: {nic.NetworkInterfaceType}");
            Console.WriteLine($"Adres MAC: {nic.GetPhysicalAddress()}");
            Console.WriteLine(new string('-', 40));
        }
    }
}
