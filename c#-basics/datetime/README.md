# c# datetime
csharp datetime notes

## today, now, utcnow
unlike Python today and now are not the same...
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime today = DateTime.Today;
            Console.WriteLine(today.ToString()); //28.12.2024 00:00:00

            DateTime now = DateTime.Now;
            Console.WriteLine(now.ToString()); //28.12.2024 13:46:41

            DateTime utcNow = DateTime.UtcNow;
            Console.WriteLine(utcNow.ToString()); //28.12.2024 12:47:27
        }
    }
}
```

## time
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime now = DateTime.Now;
            Console.WriteLine($"Time:>{now.Hour}:{now.Minute}:{now.Second}"); //Time:>13:50:47
        }
    }
}
```

## time and padleft 0
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime now = DateTime.Now;
            string hour = now.Hour.ToString().PadLeft(2, '0');
            string minute = now.Minute.ToString().PadLeft(2, '0');
            string second = now.Second.ToString().PadLeft(2, '0');
            Console.WriteLine($"Time:>{hour}:{minute}:{second}"); //Time:>13:54:09
        }
    }
}
```

## full date
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime now = DateTime.Now;
            string hour = now.Hour.ToString().PadLeft(2, '0');
            string minute = now.Minute.ToString().PadLeft(2, '0');
            string second = now.Second.ToString().PadLeft(2, '0');
            Console.WriteLine($"Time:>{hour}:{minute}:{second}"); //Time:>13:56:56
            Console.WriteLine($"Date:{now.Year}-{now.Month}-{now.Day}"); //Date:2024-12-28
        }
    }
}
```

## new datetime
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime newYear = new DateTime(2025, 1, 1);
            string hour = newYear.Hour.ToString().PadLeft(2, '0');
            string minute = newYear.Minute.ToString().PadLeft(2, '0');
            string second = newYear.Second.ToString().PadLeft(2, '0');
            Console.WriteLine($"Time:>{hour}:{minute}:{second}"); //Time:>00:00:00
            Console.WriteLine($"Date:{newYear.Year}-{newYear.Month}-{newYear.Day}"); //Date:2025-1-1
        }
    }
}
```

## day of week
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime newYear = new DateTime(2025, 1, 1);
            Console.WriteLine($"New Year will be {newYear.DayOfWeek}");
        }
    }
}
```

## is leap year
```cs
using System;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime newYear = new DateTime(2025, 1, 1);
            Console.WriteLine($"New Year will be {newYear.DayOfWeek}");
            bool leap = DateTime.IsLeapYear(newYear.Year);
            if (leap)
            {
                Console.WriteLine($"New Year {newYear.Year} will be leap Year and have 366 days");
            } else
            {
                Console.WriteLine($"New Year {newYear.Year} will have 365 days");
            }
        }
    }
}
```