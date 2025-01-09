namespace ConsoleApp18
{
    using System;
    using System.Collections.Generic;

    public static class ListExtensions
    {
        /// <summary>
        /// Removes a range of items from the list and optionally inserts new items in their place.
        /// </summary>
        public static List<T> Splice<T>(this List<T> list, int start, int count, params T[] itemsToInsert)
        {
            if (start < 0 || start > list.Count)
                throw new ArgumentOutOfRangeException(nameof(start), "Start index is out of range.");
            if (count < 0 || start + count > list.Count)
                throw new ArgumentOutOfRangeException(nameof(count), "Count is out of range.");

            // Capture the removed items to return
            var removedItems = list.GetRange(start, count);

            // Remove the range from the list
            list.RemoveRange(start, count);

            // Insert new items if provided
            if (itemsToInsert != null && itemsToInsert.Length > 0)
            {
                list.InsertRange(start, itemsToInsert);
            }

            // Return the removed items
            return removedItems;
        }
    }
    class Program
    {
        static void Main()
        {
            var numbers = new List<int> { 1, 2, 3, 4, 5 };

            // Usuń dwa elementy od pozycji 1 i wstaw nowe elementy w ich miejsce
            var removedItems = numbers.Splice(1, 2, 9, 10);

            Console.WriteLine("Removed items: " + string.Join(", ", removedItems)); // Removed items: 2, 3
            Console.WriteLine("Updated list: " + string.Join(", ", numbers)); // Updated list: 1, 9, 10, 4, 5

            // Usuń elementy bez wstawiania nowych
            removedItems = numbers.Splice(2, 2);

            Console.WriteLine("Removed items: " + string.Join(", ", removedItems)); // Removed items: 10, 4
            Console.WriteLine("Updated list: " + string.Join(", ", numbers)); // Updated list: 1, 9
        }
    }
}