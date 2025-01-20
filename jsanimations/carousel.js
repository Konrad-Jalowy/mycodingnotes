class Carousel {
    constructor(container) {
      this.container = container;
      this.slides = container.querySelectorAll('.carousel-slide');
      this.prevButton = container.querySelector('.carousel-prev');
      this.nextButton = container.querySelector('.carousel-next');
      this.currentIndex = 0;
  
      if (!this.slides.length) throw new Error('No slides found in carousel');
  
      this.init();
    }
  
    init() {
      this.updateVisibility();
      this.prevButton.addEventListener('click', () => this.prev());
      this.nextButton.addEventListener('click', () => this.next());
    }
  
    updateVisibility() {
      this.slides.forEach((slide, index) => {
        slide.style.display = index === this.currentIndex ? 'block' : 'none';
      });
    }
  
    prev() {
      this.currentIndex = (this.currentIndex - 1 + this.slides.length) % this.slides.length;
      this.updateVisibility();
    }
  
    next() {
      this.currentIndex = (this.currentIndex + 1) % this.slides.length;
      this.updateVisibility();
    }
  }
  
  // Użycie:
  new Carousel(document.querySelector('.carousel'));