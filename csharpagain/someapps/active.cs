using System;
using System.Net.NetworkInformation;
using System.Threading.Tasks;

class Program
{
    static void Main()
    {
        string subnet = "192.168.1."; // Zmień na swoją sieć

        Parallel.For(1, 255, (i) =>
        {
            string ip = subnet + i;
            Ping ping = new Ping();
            try
            {
                PingReply reply = ping.Send(ip, 100);
                if (reply.Status == IPStatus.Success)
                {
                    Console.WriteLine($"Aktywne urządzenie: {ip}");
                }
            }
            catch { }
        });

        Console.WriteLine("Skanowanie zakończone.");
    }
}
