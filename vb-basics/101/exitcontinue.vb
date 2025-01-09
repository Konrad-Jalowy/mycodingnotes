
Module Program
    Sub Main(args As String())
        For i As Integer = 1 To 10
            If i Mod 2 = 0 Then Continue For ' Pomijamy liczby parzyste
            If i > 7 Then Exit For ' Kończymy pętlę, gdy i > 7
            Console.WriteLine($"Odd Number: {i}")
        Next
    End Sub
End Module