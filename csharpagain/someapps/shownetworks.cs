using System;
using System.Diagnostics;

class Program
{
    static void Main()
    {
        Process process = new Process();
        process.StartInfo.FileName = "netsh";
        process.StartInfo.Arguments = "wlan show networks";
        process.StartInfo.RedirectStandardOutput = true;
        process.StartInfo.UseShellExecute = false;
        process.StartInfo.CreateNoWindow = true;
        process.Start();

        string output = process.StandardOutput.ReadToEnd();
        process.WaitForExit();

        Console.WriteLine(output);
    }
}