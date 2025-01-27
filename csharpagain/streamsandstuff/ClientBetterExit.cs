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

                    while (true)
                    {
                        bytesRead = stream.Read(buffer, 0, buffer.Length);
                        if (bytesRead == 0) break; // Połączenie zostało zamknięte

                        string message = Encoding.UTF8.GetString(buffer, 0, bytesRead);
                        Console.WriteLine($"\nWiadomość od serwera: {message}");
                    }
                }
                catch (IOException)
                {
                    Console.WriteLine("Połączenie zostało zamknięte przez serwer.");
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
                    break; // Wyjście z pętli wysyłania
                }

                try
                {
                    byte[] data = Encoding.UTF8.GetBytes(message);
                    stream.Write(data, 0, data.Length);
                }
                catch (IOException)
                {
                    Console.WriteLine("Błąd wysyłania wiadomości: połączenie zostało zamknięte.");
                    break;
                }
            }

            // Zakończenie wątku odbiorczego
            try
            {
                client.Close(); // Zamknięcie klienta (automatyczne zamknięcie streamu)
                receiveThread.Join(); // Czekaj na zakończenie wątku odbiorczego
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Błąd przy zamykaniu połączenia: {ex.Message}");
            }
        }

        Console.WriteLine("Połączenie zakończone.");
    }
}
