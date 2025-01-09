Module Program
    Sub Main(args As String())
        Dim counter As Integer = 5
        Do
            Console.WriteLine(counter)
            counter -= 1
        Loop While counter > 0
    End Sub
End Module