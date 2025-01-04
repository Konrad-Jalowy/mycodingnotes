open System

[<EntryPoint>]
let main argv =
    for i in 0..argv.Length-1 do
        let person = argv.[i]
        printfn "Hello %s" person
    printfn "Program finished"
    0 