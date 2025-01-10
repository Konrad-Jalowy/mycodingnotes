Module Program
    Sub Main(args As String())
        Dim result As Integer = Factorial(5)
        Console.WriteLine($"5! = {result}") ' Wypisze: "5! = 120"
    End Sub
    Function Factorial(ByVal n As Integer) As Integer
        If n <= 1 Then
            Return 1
        Else
            Return n * Factorial(n - 1)
        End If
    End Function
End Module