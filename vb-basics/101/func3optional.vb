Module Program
    Sub Main(args As String())
        Console.WriteLine(Greet("Jan")) ' Wypisze: "Cześć, Jan!"
        Console.WriteLine(Greet("Jan", "Witaj")) ' Wypisze: "Witaj, Jan!"
    End Sub
    Function Greet(ByVal name As String, Optional ByVal greeting As String = "Cześć") As String
        Return $"{greeting}, {name}!"
    End Function
End Module