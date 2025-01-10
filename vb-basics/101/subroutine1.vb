Module Program

    Sub Main(args As String())
        Greet("Jan") ' Wywołanie funkcji
    End Sub

    Sub Greet(ByVal name As String)
        Console.WriteLine($"Cześć, {name}!")
    End Sub

End Module