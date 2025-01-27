using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;

class Server
{
    static Dictionary<TcpClient, string> clients = new Dictionary<TcpClient, string>(); // Klienci i ich nazwy
    static readonly object lockObject = new object(); // Synchronizacja dostępu do listy klientów

    static void Main()
    {
        TcpListener listener = new TcpListener(IPAddress.Loopback, 5000);
        listener.Start();
        Console.WriteLine("Serwer nasłuchuje...");

        while (true)
        {
            TcpClient client = listener.AcceptTcpClient();
            lock (lockObject) clients[client] = "Anonimowy"; // Domyślna nazwa, zanim klient poda swoją
            Console.WriteLine("Nowy klient połączony.");

            // Powiadom wszystkich o nowym kliencie
            BroadcastMessage("Nowy klient dołączył do czatu.", client);

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

                    if (message.StartsWith("/name "))
                    {
                        string newName = message.Substring(6).Trim();
                        lock (lockObject) clients[client] = newName;
                        BroadcastMessage($"{newName} dołączył do czatu.", client);
                        continue;
                    }

                    lock (lockObject)
                    {
                        if (clients.TryGetValue(client, out string senderName))
                        {
                            BroadcastMessage($"{senderName}: {message}", client);
                        }
                    }
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
            lock (lockObject)
            {
                if (clients.TryGetValue(client, out string clientName))
                {
                    clients.Remove(client);
                    BroadcastMessage($"{clientName} opuścił czat.", client);
                }
            }
            Console.WriteLine("Klient rozłączony.");
        }
    }

    static void BroadcastMessage(string message, TcpClient sender)
    {
        byte[] data = Encoding.UTF8.GetBytes(message);

        lock (lockObject)
        {
            foreach (var client in clients.Keys)
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
