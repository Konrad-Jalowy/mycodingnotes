Document.prototype.myGetElementById = function(id) {
    
    var result = null;
    function traverse(node) {
      if(node == null) 
        return;
      if(node.id === id) {
            result = node;
            return;
        }
      for(var child of node.children) 
        traverse(child);
    }
    traverse(this.documentElement); 
    return result;
  }