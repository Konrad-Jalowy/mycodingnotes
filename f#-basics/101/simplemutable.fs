open System

[<EntryPoint>]
let main argv =
    let mutable firstname = "Stranger"
    if argv.Length > 0 then 
        firstname <- argv.[0]
    printfn "Hello %s" firstname
    0 