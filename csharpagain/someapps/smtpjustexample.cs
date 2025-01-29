using System;
using System.Net;
using System.Net.Mail;

class Program
{
    static void Main()
    {
        MailMessage mail = new MailMessage();
        mail.From = new MailAddress("your@email.com");
        mail.To.Add("recipient@email.com");
        mail.Subject = "Test";
        mail.Body = "To jest wiadomość testowa.";

        SmtpClient client = new SmtpClient("smtp.example.com");
        client.Credentials = new NetworkCredential("username", "password");
        client.EnableSsl = true;

        client.Send(mail);
        Console.WriteLine("Wiadomość wysłana!");
    }
}
