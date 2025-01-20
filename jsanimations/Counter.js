class Counter {
    constructor(node, startValue, endValue, duration) {
      this.node = node;
      this.startValue = startValue;
      this.endValue = endValue;
      this.duration = duration;
    }
  
    start() {
      this.startTime = performance.now();
      this.frameId = requestAnimationFrame(() => this.update());
    }
  
    update() {
      const timePassed = performance.now() - this.startTime;
      const progress = Math.min(timePassed / this.duration, 1);
      const currentValue = Math.floor(
        this.startValue + progress * (this.endValue - this.startValue)
      );
  
      this.node.textContent = currentValue;
  
      if (progress < 1) {
        this.frameId = requestAnimationFrame(() => this.update());
      }
    }
  }
  
  // Użycie:
  const counter = new Counter(document.querySelector(".counter"), 0, 100, 2000);
  counter.start();
  