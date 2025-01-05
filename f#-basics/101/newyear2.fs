open System

[<EntryPoint>]
let main argv =
    let today = DateTime.Now
    let newYear = new DateTime(today.Year+1, 1, 1)
    let difference = (newYear - today)
    printfn "%d days till New Year %d" difference.Days newYear.Year
    printfn "and %d hours %d minutes %d seconds" difference.Hours difference.Minutes difference.Seconds
    0 