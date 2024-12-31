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
