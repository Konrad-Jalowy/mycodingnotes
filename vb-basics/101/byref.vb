Module Program
    Sub Main(args As String())
        Dim myNumber As Integer = 10
        Console.WriteLine($"Przed: {myNumber}") ' Wyświetli 10
        ChangeValue(myNumber)
        Console.WriteLine($"Po: {myNumber}")    ' Wyświetli 42 (oryginał został zmieniony)
    End Sub
    Sub ChangeValue(ByRef number As Integer)
        number = 42 ' Zmieniamy oryginalną wartość
    End Sub
End Module