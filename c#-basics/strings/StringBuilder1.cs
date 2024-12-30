using System;
using System.Text;

namespace ConsoleApp12
{
   
    class Program
    {
        static void Main(string[] args)
        {
            string[] words = new string[] { "The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog" };
            StringBuilder builder = new StringBuilder();

            Console.WriteLine(builder.Length); //0
            Console.WriteLine(builder.Capacity); //16

            foreach (string word in words)
            {
                builder.Append(word);
                builder.Append(" ");
            }

            Console.WriteLine(builder.ToString()); //The quick brown fox jumps over the lazy dog

            Console.WriteLine(builder.Length); //44
            Console.WriteLine(builder.Capacity); //62
        }
        
    }    
}
