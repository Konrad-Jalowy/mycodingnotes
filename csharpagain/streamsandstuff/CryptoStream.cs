using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;

class Program
{
    static void Main()
    {
        string filePath = "encryptedData.dat";
        string dataToEncrypt = "Witaj, dane zaszyfrowane w strumieniu!";
        string password = "securePassword123";

        // Szyfrowanie danych
        using (Aes aes = Aes.Create())
        {
            aes.Key = Encoding.UTF8.GetBytes(password.PadRight(32).Substring(0, 32));
            aes.IV = new byte[16]; // Domyślne IV (zazwyczaj należy je generować losowo)

            using (FileStream fs = new FileStream(filePath, FileMode.Create))
            using (CryptoStream cryptoStream = new CryptoStream(fs, aes.CreateEncryptor(), CryptoStreamMode.Write))
            using (StreamWriter writer = new StreamWriter(cryptoStream))
            {
                writer.Write(dataToEncrypt);
            }
        }

        // Deszyfrowanie danych
        using (Aes aes = Aes.Create())
        {
            aes.Key = Encoding.UTF8.GetBytes(password.PadRight(32).Substring(0, 32));
            aes.IV = new byte[16];

            using (FileStream fs = new FileStream(filePath, FileMode.Open))
            using (CryptoStream cryptoStream = new CryptoStream(fs, aes.CreateDecryptor(), CryptoStreamMode.Read))
            using (StreamReader reader = new StreamReader(cryptoStream))
            {
                string decryptedData = reader.ReadToEnd();
                Console.WriteLine($"Odszyfrowane dane: {decryptedData}");
            }
        }
    }
}
