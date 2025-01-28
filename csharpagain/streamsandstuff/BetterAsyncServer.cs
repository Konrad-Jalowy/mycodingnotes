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
                    var response = new Dictionary<string, string>
                {
                    { "type", "message" },
                    { "username", username },
                    { "content", content }
                };
                    await BroadcastMessage(response, client);
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

    static async Task BroadcastMessage(Dictionary<string, string> message, TcpClient sender)
    {
        string json = JsonSerializer.Serialize(message);
        byte[] messageBytes = Encoding.UTF8.GetBytes(json);

        List<TcpClient> clientCopies;

        // Tworzymy kopię klientów w bloku lock
        lock (clients)
        {
            clientCopies = new List<TcpClient>(clients.ConvertAll(c => c.TcpClient));
        }

        // Wysyłamy wiadomości poza blokiem lock
        foreach (var client in clientCopies)
        {
            if (client == sender) continue;

            try
            {
                NetworkStream stream = client.GetStream();
                await stream.WriteAsync(messageBytes, 0, messageBytes.Length);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Błąd podczas wysyłania wiadomości: {ex.Message}");
            }
        }
    }

}

class ClientInfo
{
    public string Username { get; set; }
    public TcpClient TcpClient { get; set; }
}
