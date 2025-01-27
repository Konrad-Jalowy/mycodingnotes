using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

class Server
{
    static void Main()
    {
        TcpListener listener = new TcpListener(IPAddress.Loopback, 5000);
        listener.Start();
        Console.WriteLine("Serwer nasłuchuje...");

        while (true) // Pętla nasłuchująca na nowe połączenia
        {
            using (TcpClient client = listener.AcceptTcpClient())
            using (NetworkStream stream = client.GetStream())
            {
                Console.WriteLine("Połączono z klientem.");

                byte[] buffer = new byte[1024];
                int bytesRead;

                // Pętla obsługująca wiele wiadomości w ramach jednego połączenia
                while ((bytesRead = stream.Read(buffer, 0, buffer.Length)) > 0)
                {
                    string message = Encoding.UTF8.GetString(buffer, 0, bytesRead);
                    Console.WriteLine($"Otrzymano: {message}");

                    // Wyślij odpowiedź do klienta
                    string response = $"Otrzymałem twoją wiadomość: {message}";
                    byte[] responseBytes = Encoding.UTF8.GetBytes(response);
                    stream.Write(responseBytes, 0, responseBytes.Length);
                }

                Console.WriteLine("Klient zakończył połączenie.");
            }
        }
    }
}
