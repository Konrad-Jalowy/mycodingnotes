using System;
using System.Net;
using System.Net.Mail;

class Program
{
    static void Main()
    {
        string smtpServer = "mail.twojadomena.com";  // Twój serwer SMTP
        int smtpPort = 587;
        string fromEmail = "kontakt@twojadomena.com";
        string fromPassword = "TwojeHaslo";
        string toEmail = "odbiorca@example.com";

        try
        {
            MailMessage mail = new MailMessage();
            mail.From = new MailAddress(fromEmail);
            mail.To.Add(toEmail);
            mail.Subject = "Testowy e-mail";
            mail.Body = "Cześć! To jest testowa wiadomość wysłana przez SMTP hostingu.";

            SmtpClient client = new SmtpClient(smtpServer, smtpPort);
            client.Credentials = new NetworkCredential(fromEmail, fromPassword);
            client.EnableSsl = true;
            
            client.Send(mail);
            Console.WriteLine("E-mail wysłany!");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Błąd: " + ex.Message);
        }
    }
}
