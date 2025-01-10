Module Program
    Sub Main(args As String())
        PrintEvenNumbers(10)
    End Sub
    Sub PrintEvenNumbers(ByVal max As Integer)
        For i As Integer = 1 To max
            If i Mod 2 = 0 Then
                Console.WriteLine(i)
            End If
        Next
    End Sub
End Module