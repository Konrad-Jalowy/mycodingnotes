namespace ConsoleApp18
{
    public class Book
    {
        public string Title { get; }

        public Book(string title)
        {
            Title = title;
        }
    }
    public class Library : IEnumerable<Book>
    {
        private List<Book> books = new List<Book>();

        public void AddBook(Book book)
        {
            books.Add(book);
        }

        public IEnumerator<Book> GetEnumerator()
        {
            foreach (var book in books)
            {
                yield return book;
            }
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }

    class Program
    {
        static void Main()
        {
            var library = new Library();
            library.AddBook(new Book("1984"));
            library.AddBook(new Book("Brave New World"));
            library.AddBook(new Book("Fahrenheit 451"));

            foreach (var book in library)
            {
                Console.WriteLine(book.Title);
            }
        }
    }
}