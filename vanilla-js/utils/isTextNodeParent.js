function isTextNodeParent(el){
    let childNodes = Array.from(el.childNodes);
    return childNodes.some((el) => el.nodeType == Node.TEXT_NODE);
}