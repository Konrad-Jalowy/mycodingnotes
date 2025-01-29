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
            new User { Name = "Marek", Age = 40 },
            new User { Name = "Basia", Age = 20 }
        };

        var sortedUsers = users.Where(u => u.Age > 25).OrderByDescending(u => u.Age);

        foreach (var user in sortedUsers)
        {
            Console.WriteLine($"{user.Name}, {user.Age} lat");
        }
    }
}
