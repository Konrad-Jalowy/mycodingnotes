open System

let sayHello person =
    printfn "Hello %s" person

[<EntryPoint>]
let main argv =
    argv |> Array.iter sayHello 
    printfn "Program finished"
    0 