using System;
using System.Linq;
using System.Collections.Generic;

class Program
{
    class User
    {
        public string Name { get; set; }
        public int Age { get; set; }
    }

    static void Main()
    {
        List<User> users = new List<User>
        {
            new User { Name = "Adam", Age = 30 },
            new User { Name = "Ewa", Age = 25 },
            new User { Name = "Marek", Age = 40 }
        };

        var youngUsers = users.Where(u => u.Age < 35).OrderBy(u => u.Name).ToList();

        foreach (var user in youngUsers)
        {
            Console.WriteLine($"User: {user.Name}, Age: {user.Age}");
        }
    }
}
