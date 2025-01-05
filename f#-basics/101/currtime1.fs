open System

[<EntryPoint>]
let main argv =
    let time = DateTime.Now
    printfn "%02d:%02d:%02d" time.Hour time.Minute time.Second
    0 