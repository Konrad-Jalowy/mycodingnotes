class Component {
    constructor(renderHookId, shouldRender = true) {
      this.hookId = renderHookId;
      if (shouldRender) {
        this.render();
      }
    }
  
    render() {}
  
    createRootElement(tag, cssClasses, attributes) {
      const rootElement = document.createElement(tag);
      if (cssClasses) {
        rootElement.className = cssClasses;
      }
      if (attributes && attributes.length > 0) {
        for (const attr of attributes) {
          rootElement.setAttribute(attr.name, attr.value);
        }
      }
      document.getElementById(this.hookId).append(rootElement);
      return rootElement;
    }
  }