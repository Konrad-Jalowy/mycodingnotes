class Student
{
    public string Name { get; set; }
    public List<int> Grades { get; set; }
}

class Program
{
    static void Main()
    {
        List<Student> students = new List<Student>
        {
            new Student { Name = "Kasia", Grades = new List<int> { 3, 4, 5 } },
            new Student { Name = "Marek", Grades = new List<int> { 2, 3, 3 } }
        };

        // Pobranie wszystkich ocen (SelectMany rozplątuje kolekcje w kolekcji)
        var allGrades = students.SelectMany(s => s.Grades);

        Console.WriteLine(string.Join(", ", allGrades));
    }
}
