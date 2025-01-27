using System;
using System.IO;

class Program
{
    static void Main()
    {
        string filePath = "binaryData.dat";

        // Zapis binarny
        using (BinaryWriter writer = new BinaryWriter(File.Open(filePath, FileMode.Create)))
        {
            writer.Write(42); // Integer
            writer.Write(3.14159); // Double
            writer.Write("Hello, Binary Stream!"); // String
        }

        // Odczyt binarny
        using (BinaryReader reader = new BinaryReader(File.Open(filePath, FileMode.Open)))
        {
            int intValue = reader.ReadInt32();
            double doubleValue = reader.ReadDouble();
            string stringValue = reader.ReadString();

            Console.WriteLine($"Int: {intValue}, Double: {doubleValue}, String: {stringValue}");
        }
    }
}
