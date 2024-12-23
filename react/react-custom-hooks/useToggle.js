import { useState } from "react";
export const useToggle = (initialValue) => {

    const [state, setState] = useState(() => !!initialValue);

    const toggle = () => setState((prev) => !prev);

    return [state, toggle];
};