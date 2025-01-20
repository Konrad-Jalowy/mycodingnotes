class Modal {
    constructor(trigger, modal) {
      this.trigger = trigger;
      this.modal = modal;
      this.closeButton = modal.querySelector('.modal-close');
  
      if (!(trigger instanceof HTMLElement) || !(modal instanceof HTMLElement)) {
        throw new Error('Trigger and modal must be DOM nodes');
      }
  
      this.init();
    }
  
    init() {
      this.trigger.addEventListener('click', () => this.open());
      this.closeButton.addEventListener('click', () => this.close());
      window.addEventListener('click', (e) => {
        if (e.target === this.modal) this.close();
      });
    }
  
    open() {
      this.modal.style.display = 'block';
    }
  
    close() {
      this.modal.style.display = 'none';
    }
  }
  
  // HTML Setup
  document.querySelectorAll('.modal-trigger').forEach(trigger => {
    const modalId = trigger.getAttribute('data-modal');
    const modal = document.getElementById(modalId);
    new Modal(trigger, modal);
  });
  