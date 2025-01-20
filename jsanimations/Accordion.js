class Accordion {
    constructor(container) {
      this.container = container;
      if (!(container instanceof HTMLElement)) {
        throw new Error('Container must be a DOM node');
      }
  
      this.headers = Array.from(container.querySelectorAll('.accordion-header'));
      this.init();
    }
  
    init() {
      this.headers.forEach(header => {
        header.addEventListener('click', () => this.toggle(header));
      });
    }
  
    toggle(header) {
      const content = header.nextElementSibling;
      const isOpen = header.classList.contains('open');
  
      if (isOpen) {
        content.style.maxHeight = 0;
        header.classList.remove('open');
      } else {
        content.style.maxHeight = content.scrollHeight + "px";
        header.classList.add('open');
      }
    }
  }
  
  // Użycie:
  const accordion = new Accordion(document.querySelector('.accordion'));