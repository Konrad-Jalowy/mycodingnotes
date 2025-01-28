using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    static List<ClientInfo> clients = new List<ClientInfo>();

    static void Main(string[] args)
    {
        TcpListener listener = new TcpListener(IPAddress.Loopback, 5000);
        listener.Start();
        Console.WriteLine("Serwer działa na porcie 5000. Czekam na połączenia...");

        while (true)
        {
            TcpClient client = listener.AcceptTcpClient();
            _ = HandleClient(client);
        }
    }

    static async Task HandleClient(TcpClient client)
    {
        NetworkStream stream = client.GetStream();
        byte[] buffer = new byte[1024];
        string username = null;

        try
        {
            while (true)
            {
                int byteCount = await stream.ReadAsync(buffer, 0, buffer.Length);
                if (byteCount == 0) break;

                string receivedData = Encoding.UTF8.GetString(buffer, 0, byteCount);
                Console.WriteLine("Odebrano: " + receivedData);

                var message = JsonSerializer.Deserialize<Dictionary<string, string>>(receivedData);

                if (message["type"] == "register")
                {
                    // Rejestracja użytkownika
                    username = message["username"];
                    lock (clients)
                    {
                        clients.Add(new ClientInfo { Username = username, TcpClient = client });
                    }
                    Console.WriteLine($"{username} dołączył do czatu.");
                    continue;
                }

                if (message["type"] == "message")
                {
                    string content = message["content"];
                    BroadcastMessage(new Dictionary<string, string>
                    {
                        { "type", "message" },
                        { "username", username },
                        { "content", content }
                    }, client);
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("Błąd: " + ex.Message);
        }
        finally
        {
            if (username != null)
            {
                lock (clients)
                {
                    clients.RemoveAll(c => c.TcpClient == client);
                }
                Console.WriteLine($"{username} opuścił czat.");
            }
            client.Close();
        }
    }

    static void BroadcastMessage(Dictionary<string, string> message, TcpClient sender)
    {
        string json = JsonSerializer.Serialize(message);
        byte[] messageBytes = Encoding.UTF8.GetBytes(json);

        lock (clients)
        {
            foreach (var client in clients)
            {
                if (client.TcpClient == sender) continue;

                try
                {
                    NetworkStream stream = client.TcpClient.GetStream();
                    stream.Write(messageBytes, 0, messageBytes.Length);
                }
                catch
                {
                    // Jeśli nie uda się wysłać, ignorujemy
                }
            }
        }
    }
}

class ClientInfo
{
    public string Username { get; set; }
    public TcpClient TcpClient { get; set; }
}
