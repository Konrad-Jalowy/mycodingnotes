//animacje się źle chainują to trzeba będzie poprawić

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
  
    // Fade in elements
    fadeIn(duration = 400) {
        this.elements.forEach(el => {
          if (getComputedStyle(el).display === 'none') {
            el.style.display = el.dataset.originalDisplay || 'block';
            el.style.opacity = 0; // Zaczynamy od przezroczystości 0
          }
      
          let startTime = null;
      
          const fade = (timestamp) => {
            if (!startTime) startTime = timestamp;
            const elapsed = timestamp - startTime;
            const progress = Math.min(elapsed / duration, 1);
      
            el.style.opacity = progress; // Aktualizacja opacity
      
            if (progress < 1) {
              requestAnimationFrame(fade); // Kontynuuj animację
            }
          };
      
          requestAnimationFrame(() => {
            el.style.opacity = 0; // Gwarantujemy opacity przed startem animacji
            requestAnimationFrame(fade); // Uruchom animację
          });
        });
        return this;
      }
  
    // Fade out elements
    fadeOut(duration = 400) {
        this.elements.forEach(el => {
          if (!el.dataset.originalDisplay) {
            el.dataset.originalDisplay = getComputedStyle(el).display || 'block';
          }
      
          let startTime = null;
      
          const fade = (timestamp) => {
            if (!startTime) startTime = timestamp;
            const elapsed = timestamp - startTime;
            const progress = Math.min(elapsed / duration, 1);
      
            el.style.opacity = 1 - progress; // Zmniejsz opacity
      
            if (progress < 1) {
              requestAnimationFrame(fade); // Kontynuacja animacji
            } else {
              el.style.display = 'none'; // Ukryj element po animacji
              el.style.opacity = 0; // Reset opacity dla kolejnych animacji
            }
          };
      
          requestAnimationFrame(fade);
        });
        return this;
      }
      
    // Delegate event listener
    delegate(event, selector, callback) {
      this.elements.forEach(el => {
        el.addEventListener(event, e => {
          if (e.target.matches(selector)) {
            callback(e);
          }
        });
      });
      return this;
    }
  
    // Get or set value of input elements
    val(value) {
      if (value === undefined) {
        return this.elements[0]?.value || '';
      }
      this.elements.forEach(el => (el.value = value));
      return this;
    }
  
    // Serialize form data
    serialize() {
      if (!this.elements[0] || this.elements[0].tagName !== 'FORM') {
        return '';
      }
      const formData = new FormData(this.elements[0]);
      return new URLSearchParams(formData).toString();
    }
  
    // Set or get CSS styles
    css(property, value) {
      if (typeof property === 'string' && value === undefined) {
        return this.elements[0]?.style[property] || getComputedStyle(this.elements[0])[property];
      }
      if (typeof property === 'object') {
        this.elements.forEach(el => {
          Object.entries(property).forEach(([key, val]) => (el.style[key] = val));
        });
      } else {
        this.elements.forEach(el => (el.style[property] = value));
      }
      return this;
    }
  
    // Get specific element by index
    eq(index) {
      const el = this.elements[index] || null;
      return new DomWrapper(el);
    }
  
    // Get previous sibling elements
    prev() {
      const prevElements = this.elements.map(el => el.previousElementSibling).filter(el => el !== null);
      return new DomWrapper([...new Set(prevElements)]);
    }
  
    // Get next sibling elements
    next() {
      const nextElements = this.elements.map(el => el.nextElementSibling).filter(el => el !== null);
      return new DomWrapper([...new Set(nextElements)]);
    }
  
    // Check if elements have a class
    hasClass(className) {
      return this.elements.some(el => el.classList.contains(className));
    }
  
    // Static helper for easy instantiation
    static $(selector) {
      return new DomWrapper(selector);
    }
  }
  export default DomWrapper;
