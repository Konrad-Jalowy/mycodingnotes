import { forwardRef } from "react";
const EventRFC = forwardRef(function EventRFC({idx, dates, datesFirst}, ref){
    const eventText = datesFirst ? dates[idx].event : dates[idx].date;
    return (
        <p ref={ref} className="event-rfc ani-fadein">{eventText}</p>
    )
});
export default EventRFC;