Module Program
    Sub Main(args As String())
        Dim counter As Integer = 1
        Do Until counter > 5
            Console.WriteLine($"Counter: {counter}")
            counter += 1
        Loop
    End Sub
End Module