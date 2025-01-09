Module Program
    Sub Main(args As String())
        Dim numbers As Integer() = {1, 2, 3, 4, 5}
        For Each num As Integer In numbers
            Console.WriteLine($"Number: {num}")
        Next
    End Sub
End Module