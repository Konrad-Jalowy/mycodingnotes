open System

[<EntryPoint>]
let main argv =
    let dateNow = DateTime.Now
    printfn "%s" (dateNow.ToString "yyyy/MM/dd")
    0 