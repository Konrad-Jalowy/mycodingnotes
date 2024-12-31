# Vanilla JS utils
Vanilla js utils

## getTextNodes
Recursive helper function to get all text nodes
```js
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
```

## defer
timeout could be 0, it does not matter
```js
const defer = (fn, ...args) => setTimeout(fn, 1, ...args);
```
## isMatch func
Pass node and selector, get back if its match
```js
function isMatch(node, selector) {
    if(node.matches) { 
      return node.matches(selector);
    } else { 
      var matches = Element.prototype.matchesSelector || 
        Element.prototype.mozMatchesSelector ||
        Element.prototype.msMatchesSelector || 
        Element.prototype.oMatchesSelector || 
        Element.prototype.webkitMatchesSelector;
      return matches.call(node, selector);
    }
  }
```

## isAnchor
```js
function isAnchor(el){
    return el instanceof HTMLAnchorElement;
}
```

## isNewTabAnchor
```js
function isNewTabAnchor(el){
    return el.matches('a[target="_blank"]') || el.matches('a[target="blank"]');
}
```

## isScrollableAnchor
```js
function isScrollableAnchor(el){
    return el.matches('a[href^="#"]') && (document.querySelector(el.getAttribute("href")) !== null);
}
```

## isTelAnchor
```js
function isTelAnchor(el){
    return el.matches('a[href^="tel:"]');
}
```

## isTextNodeParent
```js
function isTextNodeParent(el){
    let childNodes = Array.from(el.childNodes);
    return childNodes.some((el) => el.nodeType == Node.TEXT_NODE);
}
```

## isValidTagname
theres more than one way to do that
```js
function isValidTagname(tagname) {
    return document.createElement(tagname).toString() != "[object HTMLUnknownElement]";
  }
```

## isImageMapLink
```js
function isImageMapLink(el){
    return el.matches("map > area[href]");
}
```

## isHTMLTag
```js
function isHTMLTag(value) {
    return (
        typeof value === "string" &&
        value.charAt(0) === "<" && value.charAt(value.length - 1) === ">"
    );
}
```

## isGenerator
```js
function isGenerator(fn) {
    return fn.constructor.name === 'GeneratorFunction';
}
```

## isEmptyElement
```js
function isEmptyElement(el){
    return Array.from(el.childNodes).length === 0;
}
```

## isDOMNode
```js
function isDOMNode(value) {
    return (
        typeof value === "object" &&
        value instanceof Element
    );
}
```

## isConcatenable
```js
function isConcatenable(obj){
    return Object.getPrototypeOf(obj).hasOwnProperty("concat");
}
```

## isArrowFunc
```js
function isArrowFunc(func){
    return func.toString().includes("=>");
}
```

## elementhastextonly
```js
function elementHasTextOnly(el){
    return el.childElementCount === 0 && Array.from(el.childNodes).length === 1
}
```