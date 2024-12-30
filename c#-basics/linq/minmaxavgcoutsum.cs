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
