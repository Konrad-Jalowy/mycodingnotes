
open System

[<EntryPoint>]
let main argv =
    for person in argv do
        printfn "Hello %s" person
    printfn "Program finished"
    0 