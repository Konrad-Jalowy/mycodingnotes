using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            Stack<char> characters = new Stack<char>();
            if(characters.TryPeek(out char lastOne))
            {
                Console.WriteLine(lastOne);
            } else
            {
                Console.WriteLine("Looks like the stack is empty...");
            }

            string msg = "abc!";        
            
            foreach(char c in msg)
            {
                characters.Push(c);
            }

            if(characters.TryPop(out char poppedOne))
            {
                Console.WriteLine($"Popped char : {poppedOne}");
            }            
        }
        
    }
}