using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;

class Server
{
    static List<TcpClient> clients = new List<TcpClient>();
    static readonly object lockObject = new object();

    static void Main()
    {
        TcpListener listener = new TcpListener(IPAddress.Loopback, 5000);
        listener.Start();
        Console.WriteLine("Serwer nasłuchuje...");

        while (true)
        {
            TcpClient client = listener.AcceptTcpClient();
            lock (lockObject) clients.Add(client);
            Console.WriteLine("Nowy klient połączony.");

            new Thread(() => HandleClient(client)).Start();
        }
    }

    static void HandleClient(TcpClient client)
    {
        try
        {
            using (NetworkStream stream = client.GetStream())
            {
                byte[] buffer = new byte[1024];
                int bytesRead;

                while ((bytesRead = stream.Read(buffer, 0, buffer.Length)) > 0)
                {
                    string message = Encoding.UTF8.GetString(buffer, 0, bytesRead);
                    Console.WriteLine($"Otrzymano: {message}");

                    BroadcastMessage(message, client);
                }
            }
        }
        catch (IOException)
        {
            Console.WriteLine("Klient niespodziewanie zakończył połączenie.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Wystąpił błąd: {ex.Message}");
        }
        finally
        {
            lock (lockObject) clients.Remove(client);
            Console.WriteLine("Klient rozłączony.");
        }
    }

    static void BroadcastMessage(string message, TcpClient sender)
    {
        byte[] data = Encoding.UTF8.GetBytes(message);

        lock (lockObject)
        {
            foreach (var client in clients)
            {
                if (client != sender)
                {
                    try
                    {
                        client.GetStream().Write(data, 0, data.Length);
                    }
                    catch
                    {
                        Console.WriteLine("Błąd wysyłania wiadomości.");
                    }
                }
            }
        }
    }
}
