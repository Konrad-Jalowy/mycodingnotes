using System;
using System.Collections.Generic;
using System.Linq;

class Employee
{
    public string Department { get; set; }
    public string Name { get; set; }
}

class Program
{
    static void Main()
    {
        List<Employee> employees = new List<Employee>
        {
            new Employee { Name = "Anna", Department = "IT" },
            new Employee { Name = "Bartek", Department = "HR" },
            new Employee { Name = "Celina", Department = "IT" },
            new Employee { Name = "Daniel", Department = "HR" }
        };

        var groupedEmployees = from e in employees
                               group e by e.Department into g
                               select new { Department = g.Key, Employees = g.ToList() };

        foreach (var group in groupedEmployees)
        {
            Console.WriteLine($"Dział: {group.Department}");
            foreach (var emp in group.Employees)
            {
                Console.WriteLine($" - {emp.Name}");
            }
        }
    }
}