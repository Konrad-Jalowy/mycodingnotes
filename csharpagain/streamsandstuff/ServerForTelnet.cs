using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Uruchamianie serwera...");

        TcpListener listener = new TcpListener(IPAddress.Loopback, 5000);
        listener.Start();
        Console.WriteLine("Serwer działa na porcie 5000. Czekam na połączenia...");

        while (true)
        {
            TcpClient client = listener.AcceptTcpClient();
            Console.WriteLine("Klient połączony!");
            _ = HandleClient(client); // Obsługuj klienta w osobnym wątku/Tasku.
        }
    }

    static async Task HandleClient(TcpClient client)
    {
        NetworkStream stream = client.GetStream();
        byte[] buffer = new byte[1024];
        StringBuilder messageBuilder = new StringBuilder();

        // Wyświetl prompt na początku.
        await stream.WriteAsync(Encoding.ASCII.GetBytes("> "));

        while (true)
        {
            try
            {
                // Odczytaj dane od klienta.
                int byteCount = await stream.ReadAsync(buffer, 0, buffer.Length);
                if (byteCount == 0) break; // Klient rozłączył się.

                string received = Encoding.ASCII.GetString(buffer, 0, byteCount);
                messageBuilder.Append(received);

                // Sprawdź, czy wiadomość zawiera '\n' (Enter w Telnecie).
                if (received.Contains("\n"))
                {
                    // Przetwarzamy pełną wiadomość.
                    string fullMessage = messageBuilder.ToString().Trim();
                    Console.WriteLine("Odebrano: " + fullMessage);

                    // Wyślij odpowiedź do klienta.
                    string response = "Serwer: " + fullMessage + "\r\n> ";
                    byte[] responseBytes = Encoding.ASCII.GetBytes(response);
                    await stream.WriteAsync(responseBytes, 0, responseBytes.Length);

                    // Wyczyść bufor wiadomości.
                    messageBuilder.Clear();
                }
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
