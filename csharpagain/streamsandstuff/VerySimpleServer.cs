using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Uruchamianie serwera...");

        // 1. Tworzymy TcpListener, który nasłuchuje na porcie 5000.
        TcpListener listener = new TcpListener(IPAddress.Loopback, 5000);
        listener.Start();
        Console.WriteLine("Serwer działa na porcie 5000. Czekam na połączenia...");

        while (true)
        {
            // 2. Czekamy na połączenie od klienta.
            TcpClient client = listener.AcceptTcpClient();
            Console.WriteLine("Klient połączony!");

            // 3. Obsługujemy klienta w osobnej metodzie.
            HandleClient(client);
        }
    }

    static void HandleClient(TcpClient client)
    {
        // Uzyskujemy strumień do komunikacji.
        NetworkStream stream = client.GetStream();
        byte[] buffer = new byte[1024];

        while (true)
        {
            try
            {
                // Odbieramy dane od klienta.
                int byteCount = stream.Read(buffer, 0, buffer.Length);
                if (byteCount == 0) break; // Klient zakończył połączenie.

                string message = Encoding.UTF8.GetString(buffer, 0, byteCount);
                Console.WriteLine("Odebrano: " + message);

                // Wysyłamy odpowiedź do klienta.
                string response = "Serwer: " + message;
                byte[] responseBytes = Encoding.UTF8.GetBytes(response);
                stream.Write(responseBytes, 0, responseBytes.Length);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Błąd: " + ex.Message);
                break;
            }
        }

        client.Close();
        Console.WriteLine("Klient rozłączył się.");
    }
}
