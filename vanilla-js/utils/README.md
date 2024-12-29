# Vanilla JS utils
Vanilla js utils

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