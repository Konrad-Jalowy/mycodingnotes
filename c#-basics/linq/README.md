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

## LastOrDefault
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

            Employee firstDev = employees.FirstOrDefault(emp => emp.Job == "Developer");

            if(firstDev != null)
            {
                Console.WriteLine(firstDev.EmpID + ", " + firstDev.EmpName);
            }

            Employee lastDev = employees.LastOrDefault(emp => emp.Job == "Developer");

            if (lastDev != null)
            {
                Console.WriteLine(lastDev.EmpID + ", " + lastDev.EmpName);
            }

        }
        
    }    
}
```
## element at
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

            Employee firstDev = employees.FirstOrDefault(emp => emp.Job == "Developer");

            if(firstDev != null)
            {
                Console.WriteLine(firstDev.EmpID + ", " + firstDev.EmpName);
            }

            Employee secondDev = employees.Where(emp => emp.Job == "Developer").ElementAtOrDefault(1);

            if(secondDev != null)
            {
                Console.WriteLine(secondDev.EmpID + ", " + secondDev.EmpName);
            }

        }
        
    }    
}
```

## Select
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

    class Person
    {
        public string PersonName { get; set; }
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

            List<Person> result = employees.Select(emp => new Person() { PersonName = emp.EmpName }).ToList();

            foreach (Person item in result)
            {
                Console.WriteLine(item.PersonName);
            }

        }
        
    }    
}
```

## Min, Max etc...
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
        public double Salary { get; set; }
    }

   
    class Program
    {
        static void Main(string[] args)
        {
            List<Employee> employees = new List<Employee>()
            {
                new Employee() { EmpID = 101, EmpName = "John Doe", Job = "Developer", Salary = 7223  },
                new Employee() { EmpID = 102, EmpName = "Jane Doe", Job = "Manager", Salary=901 },
                new Employee() { EmpID = 103, EmpName = "Jim Doe", Job = "Manager", Salary=5500 },
                new Employee() { EmpID = 104, EmpName = "Janet Doe", Job = "Developer", Salary=991 },
                new Employee() { EmpID = 105, EmpName = "Jane Json", Job = "Manager",Salary=1500 },
                new Employee() { EmpID = 106, EmpName = "Jim Xml", Job = "Developer", Salary=20000 },
            };

            double min = employees.Min(emp => emp.Salary);
            double max = employees.Max(emp => emp.Salary);
            double sum = employees.Sum(emp => emp.Salary);
            double avg = employees.Average(emp => emp.Salary);
            double cnt = employees.Count();

            Console.WriteLine("Min: " + min);
            Console.WriteLine("Max: " + max);
            Console.WriteLine("Sum: " + sum);
            Console.WriteLine("Average: " + avg);
            Console.WriteLine("Count: " + cnt);

        }
        
    }    
}
```

## Linq any
```cs
namespace ConsoleApp13
{
    class Program
    {
        
        static void Main(string[] args)
        {
            var numbers = new[] { 1, 2, 3, 4, 5, 6 };

            bool isAnyLargetThanFive = numbers.Any(n => n > 5);

            Console.WriteLine(isAnyLargetThanFive); //True

        }
    }
}
```

## Linq all
```cs
namespace ConsoleApp13
{
    class Program
    {
        
        static void Main(string[] args)
        {
            var numbers = new[] { 1, 2, 3, 4, 5, 6 };

            bool allGreaterThanFive = numbers.All(n => n > 5);
            bool allLessThanTen = numbers.All(n => n < 10);

            Console.WriteLine(allGreaterThanFive); //False
            Console.WriteLine(allLessThanTen); //True
        }
    }
}
```