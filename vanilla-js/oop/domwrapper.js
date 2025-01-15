class DomWrapper {
    constructor(selector) {
      if (typeof selector === 'string') {
        this.elements = Array.from(document.querySelectorAll(selector));
      } else if (selector instanceof HTMLElement) {
        this.elements = [selector];
      } else if (selector instanceof NodeList || Array.isArray(selector)) {
        this.elements = Array.from(selector);
      } else {
        this.elements = [];
      }
    }
  
    // Add a class to all elements
    addClass(className) {
      this.elements.forEach(el => el.classList.add(className));
      return this; // for chaining
    }
  
    // Remove a class from all elements
    removeClass(className) {
      this.elements.forEach(el => el.classList.remove(className));
      return this;
    }
  
    // Toggle a class on all elements
    toggleClass(className) {
      this.elements.forEach(el => el.classList.toggle(className));
      return this;
    }
  
    // Set or get attribute
    attr(attribute, value) {
      if (value === undefined) {
        return this.elements[0] ? this.elements[0].getAttribute(attribute) : null;
      }
      this.elements.forEach(el => el.setAttribute(attribute, value));
      return this;
    }
  
    // Set or get text content
    text(content) {
      if (content === undefined) {
        return this.elements[0] ? this.elements[0].textContent : '';
      }
      this.elements.forEach(el => (el.textContent = content));
      return this;
    }
  
    // Set or get HTML content
    html(content) {
      if (content === undefined) {
        return this.elements[0] ? this.elements[0].innerHTML : '';
      }
      this.elements.forEach(el => (el.innerHTML = content));
      return this;
    }
  
    // Append content to elements
    append(content) {
      this.elements.forEach(el => {
        if (content instanceof HTMLElement) {
          el.appendChild(content.cloneNode(true));
        } else if (typeof content === 'string') {
          el.insertAdjacentHTML('beforeend', content);
        }
      });
      return this;
    }
  
    // Add event listener
    on(event, callback) {
      this.elements.forEach(el => el.addEventListener(event, callback));
      return this;
    }
  
    // Remove event listener
    off(event, callback) {
      this.elements.forEach(el => el.removeEventListener(event, callback));
      return this;
    }
  
    // Find child elements
    find(selector) {
      const foundElements = [];
      this.elements.forEach(el => {
        foundElements.push(...el.querySelectorAll(selector));
      });
      return new DomWrapper(foundElements);
    }
  
    // Get parent elements
    parent() {
      const parents = this.elements.map(el => el.parentElement).filter(el => el !== null);
      return new DomWrapper([...new Set(parents)]);
    }
  
    // Static helper for easy instantiation
    static $(selector) {
      return new DomWrapper(selector);
    }
  }
  
  // Usage example:
  // const $ = DomWrapper.$;
  // $('.my-class').addClass('new-class').text('Hello World');
  