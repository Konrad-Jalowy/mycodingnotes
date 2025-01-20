export class RotateAnimation {
    constructor(node) {
      this.node = node;
    }
  
    start(duration, degrees) {
      this.duration = duration;
      this.totalDegrees = degrees;
      this.onProgress(0);
      this.startTime = performance.now();
      this.frameId = requestAnimationFrame(() => this.onFrame());
    }
  
    onFrame() {
      const timePassed = performance.now() - this.startTime;
      const progress = Math.min(timePassed / this.duration, 1);
      this.onProgress(progress);
  
      if (progress < 1) {
        this.frameId = requestAnimationFrame(() => this.onFrame());
      }
    }
  
    onProgress(progress) {
      const rotation = progress * this.totalDegrees;
      this.node.style.transform = `rotate(${rotation}deg)`;
    }
  
    stop() {
      cancelAnimationFrame(this.frameId);
    }
  }
  