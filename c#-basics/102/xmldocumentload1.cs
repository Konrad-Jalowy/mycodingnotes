using System.Xml;
namespace ConsoleApp13
{
    class Program
    {
        static void Main(string[] args)
        {
            string fileName = @"C:\csharpoutput\xmlfile.xml";
            XmlDocument xmlDoc = new XmlDocument();
            xmlDoc.Load(fileName);
            Console.WriteLine(xmlDoc.OuterXml);
        }
    }
}