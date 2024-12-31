using System.Xml.Linq;
namespace ConsoleApp13
{
    class Program
    {
        
        static void Main(string[] args)
        {
            string fileName = @"C:\csharpoutput\xmlfile.xml";
            XElement xmlDoc = XElement.Load(fileName);
            Console.WriteLine(xmlDoc.ToString());
        }
    }
}
