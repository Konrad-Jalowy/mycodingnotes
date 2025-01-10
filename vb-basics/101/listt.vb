Module Program
    Sub Main(args As String())
        Dim names As New List(Of String)()
        names.Add("Alice")
        names.Add("Bob")
        Console.WriteLine(names(1)) ' Wyświetli: Bob
    End Sub
End Module