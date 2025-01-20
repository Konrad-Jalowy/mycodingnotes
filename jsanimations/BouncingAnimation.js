export class BounceAnimation {
    constructor(node) {
      this.node = node;
    }
  
    start(duration) {
      this.duration = duration;
      this.startTime = performance.now();
      this.frameId = requestAnimationFrame(() => this.onFrame());
    }
  
    onFrame() {
      const timePassed = performance.now() - this.startTime;
      const progress = Math.min(timePassed / this.duration, 1);
  
      // Funkcja easing dla efektu bouncing
      const bounce = Math.sin(progress * Math.PI * 2) * (1 - progress);
      this.onProgress(bounce);
  
      if (progress < 1) {
        this.frameId = requestAnimationFrame(() => this.onFrame());
      }
    }
  
    onProgress(bounce) {
      this.node.style.transform = `translateY(${bounce * 50}px)`; // Przesunięcie o max 50px
    }
  
    stop() {
      cancelAnimationFrame(this.frameId);
    }
  }
  