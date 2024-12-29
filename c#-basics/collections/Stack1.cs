using System;
using System.Collections.Generic;
namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)
        {
            string msg = "hello world!";
            Stack<char> characters = new Stack<char>();
            foreach(char c in msg)
            {
                characters.Push(c);
            }
            Console.WriteLine(characters.Count); //12
            Console.WriteLine(characters.Peek()); //!
            Console.WriteLine(characters.Contains('w')); //True
            Console.WriteLine(characters.Contains('W')); //False
            Console.WriteLine(characters.Pop()); //!
            Console.WriteLine(characters.Count); //11
        }
        
    }
}
