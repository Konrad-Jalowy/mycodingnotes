export class ScaleAnimation {
    constructor(node) {
      this.node = node;
    }
  
    start(duration, startScale, endScale) {
      this.duration = duration;
      this.startScale = startScale;
      this.endScale = endScale;
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
      const scale = this.startScale + progress * (this.endScale - this.startScale);
      this.node.style.transform = `scale(${scale})`;
    }
  
    stop() {
      cancelAnimationFrame(this.frameId);
    }
  }
  