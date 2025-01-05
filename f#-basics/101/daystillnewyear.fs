open System

[<EntryPoint>]
let main argv =
    let today = DateTime.Now
    let newYear = new DateTime(today.Year+1, 1, 1);
    printfn "%d days till New Year %d" (newYear - today).Days newYear.Year
    0 