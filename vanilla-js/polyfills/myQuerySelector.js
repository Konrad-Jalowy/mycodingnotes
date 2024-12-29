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
  Document.prototype.myQuerySelector = function(selector) {
    
    var result = null;
    function traverse(node) {
      if(node == null) 
        return;
      if(isMatch(node, selector)) {
            result = node;
            return;
        }
      for(var child of node.children) 
        traverse(child);
    }
    traverse(this.documentElement); 
    return result;
  }