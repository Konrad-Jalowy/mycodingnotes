using System;

namespace ConsoleApp20
{
    public abstract class Shape { }
    public class Circle : Shape { public double Radius { get; set; } }
    public class Rectangle : Shape { public double Width { get; set; } public double Height { get; set; } }

    class Program
    {
        static void Main()
        {
            Shape shape = new Circle { Radius = 5 };

            string description = shape switch
            {
                Circle { Radius: > 0 } c => $"Okrąg o promieniu {c.Radius}",
                Rectangle { Width: > 0, Height: > 0 } r => $"Prostokąt {r.Width}x{r.Height}",
                _ => "Nieznany kształt"
            };

            Console.WriteLine(description);
        }
    }
}