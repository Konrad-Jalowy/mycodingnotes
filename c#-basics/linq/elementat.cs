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