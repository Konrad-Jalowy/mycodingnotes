using System;
using System.Net.Sockets;
using System.Text;

class Client
{
    static void Main()
    {
        using (TcpClient client = new TcpClient("127.0.0.1", 5000))
        using (NetworkStream stream = client.GetStream())
        {
            Console.WriteLine("Połączono z serwerem. Wpisz wiadomości do wysłania. Wpisz 'exit', aby zakończyć.");

            while (true)
            {
                // Odczyt wiadomości od użytkownika
                Console.Write("Wpisz wiadomość: ");
                string message = Console.ReadLine();

                // Sprawdzenie, czy użytkownik chce zakończyć
                if (message.ToLower() == "exit")
                {
                    Console.WriteLine("Zamykanie połączenia...");
                    break;
                }

                // Wyślij wiadomość do serwera
                byte[] data = Encoding.UTF8.GetBytes(message);
                stream.Write(data, 0, data.Length);

                // Odbierz odpowiedź od serwera
                byte[] buffer = new byte[1024];
                int bytesRead = stream.Read(buffer, 0, buffer.Length);
                string response = Encoding.UTF8.GetString(buffer, 0, bytesRead);
                Console.WriteLine($"Odpowiedź z serwera: {response}");
            }
        }
    }
}
