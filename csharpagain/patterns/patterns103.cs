using System;

class Program
{
    static void Main()
    {
        var point = (3, 4);

        string result = point switch
        {
            (0, 0) => "Początek układu współrzędnych",
            (0, _) => "Punkt na osi Y",
            (_, 0) => "Punkt na osi X",
            _ => "Inny punkt"
        };

        Console.WriteLine(result);
    }
}
