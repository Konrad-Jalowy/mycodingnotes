namespace ConsoleApp18
{
    class Program
    {
        public static int BinarySearch(int[] array, int target)
        {
            int left = 0;
            int right = array.Length - 1;

            while (left <= right)
            {
                int mid = left + (right - left) / 2;
                
                if (array[mid] == target)
                    return mid;
                
                if (array[mid] < target)
                    left = mid + 1;
                else               
                    right = mid - 1;
            }
         
            return -1;
        }
        static void Main(string[] args)
        {
            
            int[] numbers = { 1, 3, 5, 7, 9, 11, 13, 15 };

            Console.WriteLine("Podaj liczbę do znalezienia: ");
            int target = int.Parse(Console.ReadLine());

            int result = BinarySearch(numbers, target);

            if (result != -1)
                Console.WriteLine($"Liczba {target} znaleziona na indeksie {result}.");
            else
                Console.WriteLine($"Liczba {target} nie znajduje się w tablicy.");
        }
    }
}
