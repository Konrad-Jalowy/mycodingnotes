using System;
using System.Linq;
using System.Collections.Generic;

class Order
{
    public int OrderId { get; set; }
    public string Product { get; set; }
    public int CustomerId { get; set; }
}

class Customer
{
    public int CustomerId { get; set; }
    public string Name { get; set; }
}

class Program
{
    static void Main()
    {
        List<Customer> customers = new List<Customer>
        {
            new Customer { CustomerId = 1, Name = "Jan" },
            new Customer { CustomerId = 2, Name = "Alicja" }
        };

        List<Order> orders = new List<Order>
        {
            new Order { OrderId = 101, Product = "Laptop", CustomerId = 1 },
            new Order { OrderId = 102, Product = "Telefon", CustomerId = 1 },
            new Order { OrderId = 103, Product = "Tablet", CustomerId = 2 }
        };

        var customerOrders = customers.Join(orders,
            c => c.CustomerId,
            o => o.CustomerId,
            (c, o) => new { c.Name, o.Product });

        foreach (var item in customerOrders)
        {
            Console.WriteLine($"{item.Name} zamówił {item.Product}");
        }
    }
}