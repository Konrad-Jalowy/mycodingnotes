using System;
using System.Linq;
using System.Collections.Generic;

class Employee
{
    public string Name { get; set; }
    public string Department { get; set; }
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

        var groupedEmployees = employees.GroupBy(e => e.Department);

        foreach (var group in groupedEmployees)
        {
            Console.WriteLine($"Dział: {group.Key}");
            foreach (var employee in group)
            {
                Console.WriteLine($" - {employee.Name}");
            }
        }
    }
}