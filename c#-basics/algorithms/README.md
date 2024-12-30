# csharp algorithms
algorithms in c#

## Factorial Recursive
```cs
private static long GetFactorial(int number)

        {
            if(number < 0)
            {
                return -1;
            }

            if (number == 1 || number == 0)
            {
                return 1;
            }

            return number * GetFactorial(number - 1);

        }
```