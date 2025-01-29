using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

class Program
{
    static void Main()
    {                                       //use loopback if antivirus 
        TcpListener server = new TcpListener(IPAddress.Any, 8888);
        server.Start();
        Console.WriteLine("Serwer nasłuchuje na porcie 8888...");
        
        TcpClient client = server.AcceptTcpClient();
        NetworkStream stream = client.GetStream();
        
        byte[] buffer = Encoding.ASCII.GetBytes("Witaj kliencie!");
        stream.Write(buffer, 0, buffer.Length);

        client.Close();
        server.Stop();
    }
}
