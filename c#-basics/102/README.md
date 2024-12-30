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