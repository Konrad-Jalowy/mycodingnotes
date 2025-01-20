class Tabs {
    constructor(container) {
      this.container = container;
      this.tabButtons = container.querySelectorAll('.tab-button');
      this.tabContents = container.querySelectorAll('.tab-content');
  
      if (!this.tabButtons.length || !this.tabContents.length) {
        throw new Error('Tabs must have buttons and content');
      }
  
      this.init();
    }
  
    init() {
      this.tabButtons.forEach((button, index) => {
        button.addEventListener('click', () => this.showTab(index));
      });
  
      this.showTab(0); // Pokaż pierwszą zakładkę domyślnie
    }
  
    showTab(index) {
      this.tabButtons.forEach((button, i) => {
        button.classList.toggle('active', i === index);
      });
      this.tabContents.forEach((content, i) => {
        content.style.display = i === index ? 'block' : 'none';
      });
    }
  }
  
  // Użycie:
  new Tabs(document.querySelector('.tabs'));