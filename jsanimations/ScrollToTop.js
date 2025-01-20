class ScrollToTop {
    constructor(button) {
      this.button = button;
  
      if (!(button instanceof HTMLElement)) {
        throw new Error('Button must be a DOM node');
      }
  
      this.init();
    }
  
    init() {
      window.addEventListener('scroll', () => this.toggleVisibility());
      this.button.addEventListener('click', () => this.scrollToTop());
    }
  
    toggleVisibility() {
      if (window.scrollY > 200) {
        this.button.style.display = 'block';
      } else {
        this.button.style.display = 'none';
      }
    }
  
    scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }
  
  // Użycie:
  const scrollButton = document.createElement('button');
  scrollButton.innerText = '↑ Top';
  scrollButton.style.position = 'fixed';
  scrollButton.style.bottom = '20px';
  scrollButton.style.right = '20px';
  scrollButton.style.display = 'none';
  document.body.appendChild(scrollButton);
  
  new ScrollToTop(scrollButton);
  