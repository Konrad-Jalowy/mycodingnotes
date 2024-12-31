function getTextNodes(el){

    var textNodes = []
    
    function handler(node){
        if(node === null)
            return;
        
        if(node.nodeType === Node.TEXT_NODE)
            textNodes.push(node);

        if(node.nodeType !== Node.TEXT_NODE){
            node.childNodes.forEach((childNode) => {
                handler(childNode);
            });
        }
    }

    handler(el);

    return textNodes;
}