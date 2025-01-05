open System

[<EntryPoint>]
let main argv =
    let today = DateTime.Now
    let newYear = new DateTime(today.Year, 1, 1);
    printfn "%d days in current year complete" (today - newYear).Days
    0 