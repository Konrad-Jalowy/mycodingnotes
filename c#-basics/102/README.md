# csharp 102 
csharp 102 notes here

## Json serialize
### Simple serialize
```cs
using System;
using System.Text.Json;
namespace ConsoleApp13
{
    public class WeatherForecast
    {
        public DateTimeOffset Date { get; set; }
        public int TemperatureCelsius { get; set; }
        public string? Summary { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var weatherForecast = new WeatherForecast
            {
                Date = DateTime.Parse("2019-08-01"),
                TemperatureCelsius = 25,
                Summary = "Hot"
            };

            string jsonString = JsonSerializer.Serialize(weatherForecast);

            Console.WriteLine(jsonString);
        }
    }
}
```

## serialize json and write to file
```cs
using System;
using System.IO;
using System.Text.Json;
namespace ConsoleApp13
{
    public class WeatherForecast
    {
        public DateTimeOffset Date { get; set; }
        public int TemperatureCelsius { get; set; }
        public string? Summary { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var weatherForecast = new WeatherForecast
            {
                Date = DateTime.Parse("2019-08-01"),
                TemperatureCelsius = 25,
                Summary = "Hot"
            };


            string fileName = "WeatherForecast.json";
            string jsonString = JsonSerializer.Serialize(weatherForecast);

            File.WriteAllText(fileName, jsonString);

            Console.WriteLine(File.ReadAllText(fileName));
        }
    }
}
```
## Super-simple json read
```cs
using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
namespace ConsoleApp13
{
    class Program
    {
        static void Main(string[] args)
        {
           
            string fileName = @"C:\csharpoutput\somefile.json";
            using (StreamReader sr = new StreamReader(fileName))
            {
                string json = sr.ReadToEnd();
                var config = JsonSerializer.Deserialize<Dictionary<string, string>>(json);
                Console.WriteLine(config["name"]); //John Doe
                Console.WriteLine(config["age"]); //25
            }                          
        }
    }
}
```

## Read xml text
```cs
using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Xml;
namespace ConsoleApp13
{
    class Program
    {
        static void Main(string[] args)
        {
           
            string fileName = @"C:\csharpoutput\xmlfile.xml";
            XmlTextReader reader = new XmlTextReader(fileName);
            while (reader.Read())
            {
                switch (reader.NodeType)
                {
                    case XmlNodeType.Element: // The node is an element.
                        Console.Write("<" + reader.Name);

                        while (reader.MoveToNextAttribute()) // Read the attributes.
                            Console.Write(" " + reader.Name + "='" + reader.Value + "'");
                        Console.Write(">");
                        Console.WriteLine(">");
                        break;
                    case XmlNodeType.Text: //Display the text in each element.
                        Console.WriteLine(reader.Value);
                        break;
                    case XmlNodeType.EndElement: //Display the end of the element.
                        Console.Write("</" + reader.Name);
                        Console.WriteLine(">");
                        break;
                }
            }

        }
    }
}
```

## XMLDocument load and display
load xml from a filepath and display outerXML
```cs
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
```

## Some more xml
```cs
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
```

## Load xml with linq
```cs
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
```

## XML Linq Select
Some example i found on linq select + xml parse
```cs
using System;
using System.Linq;
using System.Xml.Linq;
namespace ConsoleApp13
{
    class Program
    {
        
        static void Main(string[] args)
        {
            string studentsXML =
                        @"<Students>
                            <Student>
                                <Name>Toni</Name>
                                <Age>21</Age>
                                <University>Yale</University>
                                <Semester>6</Semester>
                            </Student>
                            <Student>
                                <Name>Carla</Name>
                                <Age>17</Age>
                                <University>Yale</University>
                                <Semester>1</Semester>
                            </Student>
                            <Student>
                                <Name>Leyla</Name>
                                <Age>19</Age>
                                <University>Beijing Tech</University>
                                <Semester>3</Semester>
                            </Student>
                            <Student>
                                <Name>Frank</Name>
                                <Age>25</Age>
                                <University>Beijing Tech</University>
                                <Semester>10</Semester>
                            </Student>
                        </Students>";

            XDocument studentsXdoc = new XDocument();
            studentsXdoc = XDocument.Parse(studentsXML);

            var students = from student in studentsXdoc.Descendants("Student")
                           select new
                           {
                               Name = student.Element("Name").Value,
                               Age = student.Element("Age").Value,
                               University = student.Element("University").Value,
                               Semester = student.Element("Semester").Value
                           };

            foreach (var student in students)
            {
                Console.WriteLine("Student {0} with age {1} from University {2} is in his/her {3} Semester", student.Name, student.Age, student.University, student.Semester);
            }
        }
    }
}
```

## XDocument, XElement
```cs
using System.Xml.Linq;
namespace ConsoleApp13
{
    class Program
    {
        
        static void Main(string[] args)
        {
            string studentsXML =
                        @"<Students>
                            <Student>
                                <Name>John Doe</Name>
                                <Age>21</Age>                              
                            </Student>
                            <Student>
                                <Name>Jane Doe</Name>
                                <Age>17</Age>                               
                            </Student>
                            <Student>
                                <Name>Jim Doe</Name>
                                <Age>19</Age>
                            </Student>
                            <Student>
                                <Name>Janet Doe</Name>
                                <Age>25</Age>
                            </Student>
                        </Students>";

            XDocument studentsXdoc = new XDocument();
            studentsXdoc = XDocument.Parse(studentsXML);

            XElement studentsRoot = studentsXdoc.Root;

            Console.WriteLine(studentsRoot.ToString());
            
        }
    }
}
```

## Basics of XElement
```cs
namespace ConsoleApp13
{
    class Program
    {
        
        static void Main(string[] args)
        {
            string studentsXML =
                        @"<Students>
                            <Student>
                                <Name>John Doe</Name>
                                <Age>21</Age>                              
                            </Student>
                            <Student>
                                <Name>Jane Doe</Name>
                                <Age>17</Age>                               
                            </Student>
                            <Student>
                                <Name>Jim Doe</Name>
                                <Age>19</Age>
                            </Student>
                            <Student>
                                <Name>Janet Doe</Name>
                                <Age>25</Age>
                            </Student>
                        </Students>";

            XDocument studentsXdoc = new XDocument();
            studentsXdoc = XDocument.Parse(studentsXML);

            XElement studentsRoot = studentsXdoc.Root;

            Console.WriteLine(studentsRoot.IsEmpty); //False
            Console.WriteLine(studentsRoot.HasAttributes); //False
            Console.WriteLine(studentsRoot.FirstAttribute); //
            Console.WriteLine(studentsRoot.LastAttribute); //
            Console.WriteLine(studentsRoot.NodeType); //Element

        }
    }
}
```