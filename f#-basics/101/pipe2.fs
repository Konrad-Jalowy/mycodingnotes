open System

let sayHello person =
    printfn "Hello %s" person

let isValid person = 
    not(String.IsNullOrWhiteSpace person)

[<EntryPoint>]
let main argv =
    let validNames = argv |> Array.filter isValid
    validNames |> Array.iter sayHello 
    printfn "Program finished"
    0 