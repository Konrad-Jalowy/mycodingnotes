using System;
using System.IO;
using System.Net;

class Program
{
    static void Main()
    {
        string url = "ftp://example.com/file.txt";
        string user = "username";
        string pass = "password";
        
        FtpWebRequest request = (FtpWebRequest)WebRequest.Create(url);
        request.Method = WebRequestMethods.Ftp.DownloadFile;
        request.Credentials = new NetworkCredential(user, pass);
        
        using FtpWebResponse response = (FtpWebResponse)request.GetResponse();
        using Stream responseStream = response.GetResponseStream();
        using StreamReader reader = new StreamReader(responseStream);
        
        Console.WriteLine(reader.ReadToEnd());
    }
}
