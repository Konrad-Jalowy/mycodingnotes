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

## XElement more basics
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
            
            Console.WriteLine(studentsRoot.Name); //Students
            Console.WriteLine(studentsRoot.Value); //John Doe21Jane Doe17Jim Doe19Janet Doe25 (text)

        }
    }
}
```

## Descendants
```cs
using System;
using System.Collections.Generic;
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
            
            Console.WriteLine(studentsRoot.Name); //Students
            Console.WriteLine(studentsRoot.Value); //John Doe21Jane Doe17Jim Doe19Janet Doe25 (text)

            IEnumerable<XElement> desc = studentsRoot.Descendants("Student");
            foreach (var item in desc)
            {
                Console.WriteLine(item.ToString());
            }

        }
    }
}
```

## XML getting first element
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

            XElement? student = studentsRoot.Element("Student");
            if(student != null)
            {
                Console.WriteLine(student);
            }
            Console.WriteLine(studentsRoot.Elements("Student").First().ToString());
            
        }
    }
}
```

## Sleep
```cs
using System;
using System.Threading;
namespace ConsoleApp14
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Thread.Sleep(2000);
            Console.WriteLine("Hello World after 2 seconds!");
        }
    }
}
```

## Multiple threads
```cs
using System;
using System.Threading;
namespace ConsoleApp14
{
    class Program
    {
        static void Main(string[] args)
        {
            new Thread(() =>
            {
                Thread.Sleep(1000);
                Console.WriteLine("Thread 1");
            }).Start();

            new Thread(() =>
            {
                Thread.Sleep(1000);
                Console.WriteLine("Thread 2");
            }).Start();

            new Thread(() =>
            {
                Thread.Sleep(1000);
                Console.WriteLine("Thread 3");
            }).Start();

            new Thread(() =>
            {
                Thread.Sleep(1000);
                Console.WriteLine("Thread 4");
            }).Start();
        }
    }
}
```

## Threading basics
```cs
using System;
using System.Threading;
namespace ConsoleApp14
{
    class Program
    {
        static void Main(string[] args)
        {
            ThreadStart threadStart1 = new ThreadStart(Hello);
            Thread th1 = new Thread(threadStart1);
            th1.Start();
        }

        static void Hello()
        {
            Console.WriteLine("Hello world from thread");
        }
    }
}
```

## Threading 4
```cs
using System;
using System.Threading;
namespace ConsoleApp14
{
    class Program
    {
        static void Main(string[] args)
        {
            ThreadStart threadStart1 = new ThreadStart(CountUp);
            Thread th1 = new Thread(threadStart1);
            th1.Start();

            ThreadStart threadStart2 = new ThreadStart(CountDown);
            Thread th2 = new Thread(threadStart2);
            th2.Start();

            Console.WriteLine("Believe it or not ill run before those threads are finished");
            
        }
     
        static void CountUp()
        {
            for(int i = 0; i <= 10; i++)
            {
                Console.WriteLine(i);
                Thread.Sleep(10);
            }
            Thread.Sleep(1000);
        }

        static void CountDown()
        {
            for (int i = 20; i >= 11; i--)
            {
                Console.WriteLine(i);
                Thread.Sleep(10);
            }
            Thread.Sleep(1000);
        }
    }
}
```

## Joining threads
waiting for threads to finish
```cs
using System;
using System.Threading;
namespace ConsoleApp14
{
    class Program
    {
        static void Main(string[] args)
        {
            ThreadStart threadStart1 = new ThreadStart(CountUp);
            Thread th1 = new Thread(threadStart1);
            th1.Start();

            ThreadStart threadStart2 = new ThreadStart(CountDown);
            Thread th2 = new Thread(threadStart2);
            th2.Start();

            Console.WriteLine("Believe it or not ill run before those threads are finished");
            th1.Join();
            th2.Join();
            Console.WriteLine("Ill run when th1 and th2 are finished, not before that...");
            
        }
     
        static void CountUp()
        {
            for(int i = 0; i <= 10; i++)
            {
                Console.WriteLine(i);
                Thread.Sleep(10);
            }
            Thread.Sleep(1000);
        }

        static void CountDown()
        {
            for (int i = 20; i >= 11; i--)
            {
                Console.WriteLine(i);
                Thread.Sleep(10);
            }
            Thread.Sleep(1000);
        }
    }
}
```

## Thread priority
Its not about what thread "goes first" its about resources... here no difference bc they are similar...
still example for a reference
```cs
using System;
using System.Threading;
namespace ConsoleApp14
{
    class Program
    {
        static void Main(string[] args)
        {
            ThreadStart threadStart1 = new ThreadStart(CountUp);
            Thread th1 = new Thread(threadStart1);
            th1.Priority = ThreadPriority.Highest;
            th1.Start();

            ThreadStart threadStart2 = new ThreadStart(CountDown);
            Thread th2 = new Thread(threadStart2);
            th2.Priority = ThreadPriority.BelowNormal;
            th2.Start();

            Console.WriteLine("Believe it or not ill run before those threads are finished");
            th1.Join();
            th2.Join();
            Console.WriteLine("Ill run when th1 and th2 are finished, not before that...");
            
        }
     
        static void CountUp()
        {
            for(int i = 0; i <= 10; i++)
            {
                Console.WriteLine(i);
                Thread.Sleep(10);
            }
            Thread.Sleep(1000);
        }

        static void CountDown()
        {
            for (int i = 20; i >= 11; i--)
            {
                Console.WriteLine(i);
                Thread.Sleep(10);
            }
            Thread.Sleep(1000);
        }
    }
}
```

## Threadpool
```cs
using System;
using System.Threading;
namespace ConsoleApp14
{
    class Program
    {
        static void Main(string[] args)
        {
            ThreadPool.QueueUserWorkItem(CountUp);
            ThreadPool.QueueUserWorkItem(CountDown);
            Thread.Sleep(3000);
            Console.WriteLine("When main thread dies, threadpool items also die no matter finished or not...");
            
        }
     
        static void CountUp(Object stateInfo)
        {
            for(int i = 0; i <= 10; i++)
            {
                Console.WriteLine(i);
                Thread.Sleep(10);
            }
            Thread.Sleep(1000);
        }

        static void CountDown(Object stateInfo)
        {
            for (int i = 20; i >= 11; i--)
            {
                Console.WriteLine(i);
                Thread.Sleep(10);
            }
            Thread.Sleep(1000);
        }
    }
}
```

## Using lock + newer syntax
```cs
using System;
using System.Threading;
namespace ConsoleApp14
{
    class Program
    {
        static string Name = "john";
        static void Main(string[] args)
        {
            
            Thread th1 = new Thread(AddDoe);
            th1.Start();
  
            Thread th2 = new Thread(Capitalize);           
            th2.Start();

            Console.WriteLine("Before");
            th1.Join();
            th2.Join();
            Console.WriteLine("All threads finished");
            Console.WriteLine(Name);
        }

        static void AddDoe()
        {
            lock(Name)
            {
                Name = Name + " Doe";
            }              
        }

        static void Capitalize()
        {
            lock(Name)
            {
                Name = "John";
            }           
        }
    }
}
```

## Delegates basics
```cs
using System;
using System.Threading;
namespace ConsoleApp15
{
    
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hi!");

            WelcomePerson hiDelegate = SayHi;
            WelcomePerson helloDelegate = new WelcomePerson(SayHello); //older way

            hiDelegate("John"); //Hi John
            helloDelegate("Jane"); //Hello Jane
           
        }

        public delegate void WelcomePerson(string name);

        public static void SayHi(string name)
        {
            Console.WriteLine($"Hi {name}");
        }

        public static void SayHello(string name)
        {
            Console.WriteLine($"Hello {name}");
        }

    }
}
```

## Task basics
```cs
using System;
using System.Threading.Tasks;

namespace ConsoleApp18
{
    class Program
    {
        public static void write(char c)
        {
            int i = 1000;
            while (i-- > 0)
            {
                Console.Write(c);
            }
        }
        static void Main(string[] args)
        {
            
            Task.Factory.StartNew(() => write('.'));

            Task t = new(() => write('?'));
            t.Start();

            write('-');
        }
    }
}
```

## Task with state
```cs
namespace ConsoleApp18
{
    class Program
    {
        public static void write(object o)
        {
            int i = 1000;
            while (i-- > 0)
            {
                Console.Write(o);
            }
        }
        static void Main(string[] args)
        {
            
            Task.Factory.StartNew(write, "hello");

            Task t = new(write, "hi");
            t.Start();
        
        }
    }
}
```

## Task current id
```cs
using System;
using System.Threading.Tasks;

namespace ConsoleApp18
{
    class Program
    {
        public static void write(object o)
        {
            int i = 1000;
            while (i-- > 0)
            {
                Console.WriteLine(Task.CurrentId);
                Console.Write(o);
            }
        }
        static void Main(string[] args)
        {
            
            Task.Factory.StartNew(write, "hello");

            Task t = new(write, "hi");
            t.Start();

            write("hi");
        }
    }
}
```