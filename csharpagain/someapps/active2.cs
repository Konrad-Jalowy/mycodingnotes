using System;
using System.Net.NetworkInformation;
using System.Net;
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
                    string mac = GetMacFromArp(ip);
                    Console.WriteLine($"Aktywne urządzenie: {ip} - MAC: {mac}");
                }
            }
            catch { }
        });

        Console.WriteLine("Skanowanie zakończone.");
    }

    static string GetMacFromArp(string ipAddress)
    {
        string macAddress = "Nieznany";
        try
        {
            var p = new System.Diagnostics.Process();
            p.StartInfo.FileName = "arp";
            p.StartInfo.Arguments = "-a";
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.CreateNoWindow = true;
            p.Start();
            string output = p.StandardOutput.ReadToEnd();
            p.WaitForExit();

            string[] lines = output.Split('\n');
            foreach (string line in lines)
            {
                if (line.Contains(ipAddress))
                {
                    string[] parts = line.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
                    if (parts.Length >= 2)
                        macAddress = parts[1];
                }
            }
        }
        catch { }

        return macAddress;
    }
}
