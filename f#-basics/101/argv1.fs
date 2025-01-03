open System

[<EntryPoint>]
let main argv =
    let firstarg = argv.[0]
    printfn "First arg is %s" firstarg
    0 