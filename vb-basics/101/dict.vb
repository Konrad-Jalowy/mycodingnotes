Module Program
    Sub Main(args As String())
        Dim ages As New Dictionary(Of String, Integer)()
        ages.Add("Alice", 30)
        ages.Add("Bob", 25)
        Console.WriteLine(ages("Alice")) ' Wyświetli: 30
    End Sub
End Module