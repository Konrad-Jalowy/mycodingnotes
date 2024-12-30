# csharp linq 
csharp linq notes...

## where
```cs
using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp12
{
    class Employee
    {
        public int EmpID { get; set; }
        public string EmpName { get; set; }
        public string Job { get; set; }
        public string City { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Employee> employees = new List<Employee>()
            {
                new Employee() { EmpID = 101, EmpName = "John Doe", Job = "Developer", City = "New York" },
                new Employee() { EmpID = 102, EmpName = "Jane Doe", Job = "Manager", City = "New York" },
                new Employee() { EmpID = 103, EmpName = "Jim Doe", Job = "Manager", City = "London" },
                new Employee() { EmpID = 104, EmpName = "Janet Doe", Job = "Developer", City = "Warsaw" },
                new Employee() { EmpID = 105, EmpName = "Jane Json", Job = "Manager", City = "Warsaw" },
                new Employee() { EmpID = 106, EmpName = "Jim Xml", Job = "Developer", City = "London" },
            };

            IEnumerable<Employee> result = employees.Where(emp => emp.City == "Warsaw");
            foreach (Employee item in result)
            {
                Console.WriteLine(item.EmpID + ", " + item.EmpName + ", " + item.Job + ", " + item.City);
            }

        }
        
    }    
}
```
## using or
super simple
```cs
using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp12
{
    class Employee
    {
        public int EmpID { get; set; }
        public string EmpName { get; set; }
        public string Job { get; set; }
        public string City { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Employee> employees = new List<Employee>()
            {
                new Employee() { EmpID = 101, EmpName = "John Doe", Job = "Developer", City = "New York" },
                new Employee() { EmpID = 102, EmpName = "Jane Doe", Job = "Manager", City = "New York" },
                new Employee() { EmpID = 103, EmpName = "Jim Doe", Job = "Manager", City = "London" },
                new Employee() { EmpID = 104, EmpName = "Janet Doe", Job = "Developer", City = "Warsaw" },
                new Employee() { EmpID = 105, EmpName = "Jane Json", Job = "Manager", City = "Warsaw" },
                new Employee() { EmpID = 106, EmpName = "Jim Xml", Job = "Developer", City = "London" },
            };

            IEnumerable<Employee> result = employees.Where(emp => emp.City == "Warsaw" || emp.City == "London");
            foreach (Employee item in result)
            {
                Console.WriteLine(item.EmpID + ", " + item.EmpName + ", " + item.Job + ", " + item.City);
            }

        }
        
    }    
}
```
## orderby and chaining
```cs
using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp12
{
    class Employee
    {
        public int EmpID { get; set; }
        public string EmpName { get; set; }
        public string Job { get; set; }
        public string City { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Employee> employees = new List<Employee>()
            {
                new Employee() { EmpID = 101, EmpName = "John Doe", Job = "Developer", City = "New York" },
                new Employee() { EmpID = 102, EmpName = "Jane Doe", Job = "Manager", City = "New York" },
                new Employee() { EmpID = 103, EmpName = "Jim Doe", Job = "Manager", City = "London" },
                new Employee() { EmpID = 104, EmpName = "Janet Doe", Job = "Developer", City = "Warsaw" },
                new Employee() { EmpID = 105, EmpName = "Jane Json", Job = "Manager", City = "Warsaw" },
                new Employee() { EmpID = 106, EmpName = "Jim Xml", Job = "Developer", City = "London" },
            };

            IEnumerable<Employee> result = employees
                .Where(emp => emp.City == "Warsaw" || emp.City == "London")
                .OrderByDescending(emp => emp.EmpID);

            foreach (Employee item in result)
            {
                Console.WriteLine(item.EmpID + ", " + item.EmpName + ", " + item.Job + ", " + item.City);
            }

        }
        
    }    
}
```

## ThenBy
super simple
```cs
using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp12
{
    class Employee
    {
        public int EmpID { get; set; }
        public string EmpName { get; set; }
        public string Job { get; set; }
        public string City { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Employee> employees = new List<Employee>()
            {
                new Employee() { EmpID = 101, EmpName = "John Doe", Job = "Developer", City = "New York" },
                new Employee() { EmpID = 102, EmpName = "Jane Doe", Job = "Manager", City = "New York" },
                new Employee() { EmpID = 103, EmpName = "Jim Doe", Job = "Manager", City = "London" },
                new Employee() { EmpID = 104, EmpName = "Janet Doe", Job = "Developer", City = "Warsaw" },
                new Employee() { EmpID = 105, EmpName = "Jane Json", Job = "Manager", City = "Warsaw" },
                new Employee() { EmpID = 106, EmpName = "Jim Xml", Job = "Developer", City = "London" },
            };

            IEnumerable<Employee> result = employees
                .Where(emp => emp.City == "Warsaw" || emp.City == "London")
                .OrderBy(emp => emp.Job)
                .ThenBy(emp => emp.City);
           

            foreach (Employee item in result)
            {
                Console.WriteLine(item.EmpID + ", " + item.EmpName + ", " + item.Job + ", " + item.City);
            }

        }
        
    }    
}
```

## toList
super simple
```cs
using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp12
{
    class Employee
    {
        public int EmpID { get; set; }
        public string EmpName { get; set; }
        public string Job { get; set; }
        public string City { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Employee> employees = new List<Employee>()
            {
                new Employee() { EmpID = 101, EmpName = "John Doe", Job = "Developer", City = "New York" },
                new Employee() { EmpID = 102, EmpName = "Jane Doe", Job = "Manager", City = "New York" },
                new Employee() { EmpID = 103, EmpName = "Jim Doe", Job = "Manager", City = "London" },
                new Employee() { EmpID = 104, EmpName = "Janet Doe", Job = "Developer", City = "Warsaw" },
                new Employee() { EmpID = 105, EmpName = "Jane Json", Job = "Manager", City = "Warsaw" },
                new Employee() { EmpID = 106, EmpName = "Jim Xml", Job = "Developer", City = "London" },
            };

            List<Employee> filteredEmployees = employees.Where(emp => emp.Job == "Manager").ToList();

            Console.WriteLine(filteredEmployees.Count); //3

        }
        
    }    
}
```

## First and FirstOrDefault
```cs
using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp12
{
    class Employee
    {
        public int EmpID { get; set; }
        public string EmpName { get; set; }
        public string Job { get; set; }
        public string City { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Employee> employees = new List<Employee>()
            {
                new Employee() { EmpID = 101, EmpName = "John Doe", Job = "Developer", City = "New York" },
                new Employee() { EmpID = 102, EmpName = "Jane Doe", Job = "Manager", City = "New York" },
                new Employee() { EmpID = 103, EmpName = "Jim Doe", Job = "Manager", City = "London" },
                new Employee() { EmpID = 104, EmpName = "Janet Doe", Job = "Developer", City = "Warsaw" },
                new Employee() { EmpID = 105, EmpName = "Jane Json", Job = "Manager", City = "Warsaw" },
                new Employee() { EmpID = 106, EmpName = "Jim Xml", Job = "Developer", City = "London" },
            };

            Employee firstDev = employees.First(emp => emp.Job == "Developer");
            Console.WriteLine(firstDev.EmpID + ", "  + firstDev.EmpName);

            Employee firstLawyer = employees.FirstOrDefault(emp => emp.Job == "Lawyer");

            if(firstLawyer == null)
            {
                Console.WriteLine("No Lawyer found...");
            }

        }
        
    }    
}
```