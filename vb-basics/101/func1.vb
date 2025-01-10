Module Program
    Sub Main(args As String())
        Dim result As Integer = AddNumbers(5, 10)
        Console.WriteLine($"Wynik dodawania: {result}")
    End Sub

    Function AddNumbers(ByVal a As Integer, ByVal b As Integer) As Integer
        Return a + b
    End Function
End Module