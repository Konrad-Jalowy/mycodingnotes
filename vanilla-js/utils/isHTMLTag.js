function isHTMLTag(value) {
    return (
        typeof value === "string" &&
        value.charAt(0) === "<" && value.charAt(value.length - 1) === ">"
    );
}