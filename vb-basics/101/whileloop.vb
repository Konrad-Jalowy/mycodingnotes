Module Program
    Sub Main(args As String())
        Dim counter As Integer = 1
        While counter <= 5
            Console.WriteLine($"Counter: {counter}")
            counter += 1
        End While
    End Sub
End Module