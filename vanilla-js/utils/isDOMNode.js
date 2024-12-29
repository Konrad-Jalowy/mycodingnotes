function isDOMNode(value) {
    return (
        typeof value === "object" &&
        value instanceof Element
    );
}