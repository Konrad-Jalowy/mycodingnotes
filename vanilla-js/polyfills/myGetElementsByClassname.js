Document.prototype.myGetElementsByClassname = function(classname) {
    var result = [];
    
    function traverse(node) {
      if(node == null) 
        return;
      if(node.classList.contains(classname)) 
        result.push(node);
      for(var child of node.children) 
        traverse(child);
    }
    traverse(this.documentElement); 
    return result;
  }