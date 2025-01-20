class ProgressBar {
    constructor(node) {
      this.node = node;
    }
  
    start(duration) {
      this.duration = duration;
      this.node.style.width = "0%";
      this.startTime = performance.now();
      this.frameId = requestAnimationFrame(() => this.update());
    }
  
    update() {
      const timePassed = performance.now() - this.startTime;
      const progress = Math.min(timePassed / this.duration, 1);
      this.node.style.width = `${progress * 100}%`;
  
      if (progress < 1) {
        this.frameId = requestAnimationFrame(() => this.update());
      }
    }
  }
  
  // Użycie:
  const progressBar = new ProgressBar(document.querySelector(".progress-bar"));
  progressBar.start(2000);
  