class AdvancedTooltip {
    constructor(element, text, position = 'top') {
      this.element = element;
      this.text = text;
      this.position = position;
      this.tooltip = null;
      this.init();
    }

    static init(selector) {
      document.querySelectorAll(selector).forEach(element => {
        const position = element.getAttribute('data-position') || 'top';
        const tooltipText = element.getAttribute('data-tooltip');
        new AdvancedTooltip(element, tooltipText, position);
      });
    }

    init() {
      this.element.addEventListener('mouseenter', () => this.show());
      this.element.addEventListener('mouseleave', () => this.hide());
    }

    show() {
      this.tooltip = document.createElement('div');
      this.tooltip.className = 'tooltip tooltip-' + this.position;
      this.tooltip.innerText = this.text;
      document.body.appendChild(this.tooltip);

      const rect = this.element.getBoundingClientRect();
      const tooltipRect = this.tooltip.getBoundingClientRect();

      // Dynamic positioning
      if (this.position === 'top') {
        this.tooltip.style.top = `${rect.top - tooltipRect.height - 5 + window.scrollY}px`;
        this.tooltip.style.left = `${rect.left + rect.width / 2 - tooltipRect.width / 2 + window.scrollX}px`;
      } else if (this.position === 'right') {
        this.tooltip.style.left = `${rect.right + 5 + window.scrollX}px`;
        this.tooltip.style.top = `${rect.top + rect.height / 2 - tooltipRect.height / 2 + window.scrollY}px`;
      } else if (this.position === 'bottom') {
        this.tooltip.style.top = `${rect.bottom + 5 + window.scrollY}px`;
        this.tooltip.style.left = `${rect.left + rect.width / 2 - tooltipRect.width / 2 + window.scrollX}px`;
      } else if (this.position === 'left') {
        this.tooltip.style.left = `${rect.left - tooltipRect.width - 5 + window.scrollX}px`;
        this.tooltip.style.top = `${rect.top + rect.height / 2 - tooltipRect.height / 2 + window.scrollY}px`;
      }

      this.tooltip.classList.add('tooltip-visible');
    }

    hide() {
      if (this.tooltip) {
        this.tooltip.classList.remove('tooltip-visible');
        setTimeout(() => {
          if (this.tooltip) document.body.removeChild(this.tooltip);
          this.tooltip = null;
        }, 200);
      }
    }
  }

  // Initialize tooltips
  AdvancedTooltip.init('.tooltip-target');