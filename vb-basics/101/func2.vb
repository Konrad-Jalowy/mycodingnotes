Module Program
    Sub Main(args As String())
        Console.WriteLine($"Dzisiejsza data: {GetCurrentDate()}")
    End Sub
    Function GetCurrentDate() As String
        Return DateTime.Now.ToString("yyyy-MM-dd")
    End Function
End Module