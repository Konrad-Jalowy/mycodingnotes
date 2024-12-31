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
            XmlNode firstChild = xmlDoc.FirstChild;
            //Console.WriteLine(firstChild.InnerText);
            Console.WriteLine(firstChild.HasChildNodes); //True
            Console.WriteLine(firstChild.NodeType); //Element
            XmlElement firstChildEl = (XmlElement)firstChild;
            Console.WriteLine(firstChildEl.HasAttributes); //False
        }
    }
}
