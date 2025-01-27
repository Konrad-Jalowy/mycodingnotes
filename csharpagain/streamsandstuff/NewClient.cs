using System;
using System.IO;
using System.Net.Sockets;
using System.Text;
using System.Threading;

class Client
{
    static void Main()
    {
        using (TcpClient client = new TcpClient("127.0.0.1", 5000))
        using (NetworkStream stream = client.GetStream())
        {
            Console.WriteLine("Połączono z serwerem. Wpisz 'exit', aby zakończyć.");

            // Wątek do odbierania wiadomości
            Thread receiveThread = new Thread(() =>
            {
                try
                {
                    byte[] buffer = new byte[1024];
                    int bytesRead;

                    while ((bytesRead = stream.Read(buffer, 0, buffer.Length)) > 0)
                    {
                        string message = Encoding.UTF8.GetString(buffer, 0, bytesRead);
                        Console.WriteLine($"\nWiadomość od innego klienta: {message}");
                    }
                }
                catch (IOException)
                {
                    Console.WriteLine("Połączenie zostało zamknięte.");
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Błąd: {ex.Message}");
                }
            });

            receiveThread.Start();

            // Pętla wysyłania wiadomości
            while (true)
            {
                string message = Console.ReadLine();

                if (message.ToLower() == "exit")
                {
                    Console.WriteLine("Zamykanie połączenia...");
                    break;
                }

                byte[] data = Encoding.UTF8.GetBytes(message);
                stream.Write(data, 0, data.Length);
            }

            // Zakończenie wątku odbiorczego
            receiveThread.Join();
        }
    }
}
