open System

[<EntryPoint>]
let main argv =
    if argv.Length > 0 then 
        let firstarg = argv.[0]
        printfn "First arg is %s" firstarg
    0 