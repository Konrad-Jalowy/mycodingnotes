using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    static List<TcpClient> clients = new List<TcpClient>();

    static void Main(string[] args)
    {
        TcpListener listener = new TcpListener(IPAddress.Loopback, 5000);
        listener.Start();
        Console.WriteLine("Serwer działa na porcie 5000. Czekam na połączenia...");

        while (true)
        {
            TcpClient client = listener.AcceptTcpClient();
            clients.Add(client);
            Console.WriteLine("Klient połączony!");
            _ = HandleClient(client);
        }
    }

    static async Task HandleClient(TcpClient client)
    {
        NetworkStream stream = client.GetStream();
        byte[] buffer = new byte[1024];

        try
        {
            while (true)
            {
                int byteCount = await stream.ReadAsync(buffer, 0, buffer.Length);
                if (byteCount == 0) break;

                string receivedData = Encoding.UTF8.GetString(buffer, 0, byteCount);
                Console.WriteLine("Odebrano: " + receivedData);

                // Parsowanie JSON
                var message = JsonSerializer.Deserialize<Dictionary<string, string>>(receivedData);

                // Przetwarzanie wiadomości
                string responseContent = message["content"]; // Na razie zwracamy to samo
                var response = new Dictionary<string, string>
                {
                    { "type", "response" },
                    { "content", "Serwer otrzymał: " + responseContent }
                };

                string responseJson = JsonSerializer.Serialize(response);
                byte[] responseBytes = Encoding.UTF8.GetBytes(responseJson);

                // Wysyłanie odpowiedzi do klienta
                await stream.WriteAsync(responseBytes, 0, responseBytes.Length);
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("Błąd: " + ex.Message);
        }
        finally
        {
            clients.Remove(client);
            client.Close();
            Console.WriteLine("Klient rozłączył się.");
        }
    }
}