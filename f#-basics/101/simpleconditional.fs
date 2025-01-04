open System

[<EntryPoint>]
let main argv =
    let firstname =
        if argv.Length > 0 then 
            argv.[0]
        else
            "Stranger"
    printfn "Hello %s" firstname
    0 