class AdvancedCarousel {
    constructor(container, options = {}) {
      this.container = container;
      this.slides = container.querySelectorAll('.carousel-slide');
      this.prevButton = container.querySelector('.carousel-prev');
      this.nextButton = container.querySelector('.carousel-next');
      this.currentIndex = 0;
      this.autoplay = options.autoplay || false;
      this.interval = options.interval || 3000;

      this.init();
    }

    init() {
      this.updateVisibility();
      this.prevButton.addEventListener('click', () => this.prev());
      this.nextButton.addEventListener('click', () => this.next());

      if (this.autoplay) {
        this.startAutoplay();
        this.container.addEventListener('mouseenter', () => this.stopAutoplay());
        this.container.addEventListener('mouseleave', () => this.startAutoplay());
      }
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

    startAutoplay() {
      this.autoplayTimer = setInterval(() => this.next(), this.interval);
    }

    stopAutoplay() {
      clearInterval(this.autoplayTimer);
    }
  }

  new AdvancedCarousel(document.querySelector('.carousel'), { autoplay: true, interval: 5000 });