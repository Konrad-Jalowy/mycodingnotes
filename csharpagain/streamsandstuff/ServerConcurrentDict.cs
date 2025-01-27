using System;
using System.Collections.Concurrent;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;

class Server
{
    static ConcurrentDictionary<TcpClient, string> clients = new ConcurrentDictionary<TcpClient, string>(); // Klienci i ich nazwy

    static void Main()
    {
        TcpListener listener = new TcpListener(IPAddress.Loopback, 5000);
        listener.Start();
        Console.WriteLine("Serwer nasłuchuje...");

        while (true)
        {
            TcpClient client = listener.AcceptTcpClient();
            if (!clients.TryAdd(client, "Anonimowy"))
            {
                Console.WriteLine("Nie udało się dodać klienta.");
                continue;
            }
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
                        if (clients.TryUpdate(client, newName, clients[client]))
                        {
                            BroadcastMessage($"{newName} dołączył do czatu.", client);
                        }
                        continue;
                    }

                    if (clients.TryGetValue(client, out string senderName))
                    {
                        BroadcastMessage($"{senderName}: {message}", client);
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
            if (clients.TryRemove(client, out string clientName))
            {
                BroadcastMessage($"{clientName} opuścił czat.", client);
            }
            Console.WriteLine("Klient rozłączony.");
        }
    }

    static void BroadcastMessage(string message, TcpClient sender)
    {
        byte[] data = Encoding.UTF8.GetBytes(message);

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
