import { forwardRef } from "react";
const DateRFC = forwardRef(function DateRFC2({idx, dates, datesFirst}, ref){
    const dateText = datesFirst ? dates[idx].date : dates[idx].event
   
    return (
        <p ref={ref} className="date-rfc ani-fadein">{dateText}</p>
    );
});

export default DateRFC;