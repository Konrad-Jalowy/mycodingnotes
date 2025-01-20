class Tooltip {
    constructor(element, text) {
      this.element = element;
      this.text = text;
      this.tooltip = null;
      this.init();
    }
  
    init() {
      this.element.addEventListener('mouseenter', () => this.show());
      this.element.addEventListener('mouseleave', () => this.hide());
    }
  
    show() {
      this.tooltip = document.createElement('div');
      this.tooltip.className = 'tooltip';
      this.tooltip.innerText = this.text;
      document.body.appendChild(this.tooltip);
  
      const rect = this.element.getBoundingClientRect();
      this.tooltip.style.position = 'absolute';
      this.tooltip.style.top = `${rect.bottom + window.scrollY + 5}px`;
      this.tooltip.style.left = `${rect.left + window.scrollX}px`;
    }
  
    hide() {
      if (this.tooltip) {
        document.body.removeChild(this.tooltip);
        this.tooltip = null;
      }
    }
  }
  
  // Użycie:
  const element = document.querySelector('.tooltip-target');
  new Tooltip(element, 'This is a custom tooltip');
  
 
  