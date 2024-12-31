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
