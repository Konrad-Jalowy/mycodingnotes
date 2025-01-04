open System

let sayHello person =
    printfn "Hello %s" person

let isValid person = 
    String.IsNullOrWhiteSpace person |> not

let isAllowed person =
    person <> "jim"

[<EntryPoint>]
let main argv =
    argv 
    |> Array.filter isValid 
    |> Array.filter isAllowed
    |> Array.iter sayHello 
    printfn "Program finished"
    0 