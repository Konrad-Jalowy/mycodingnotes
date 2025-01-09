Module Program
    Sub Main(args As String())
        Dim counter As Integer = 1
        Do
            Console.WriteLine($"Counter: {counter}")
            counter += 1
        Loop Until counter > 5
    End Sub
End Module