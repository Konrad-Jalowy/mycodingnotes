export class SlideInAnimation {
    constructor(node) {
      this.node = node;
    }
  
    start(duration) {
      this.duration = duration;
      if (this.duration === 0) {
        this.onProgress(1);
      } else {
        this.onProgress(0);
        this.startTime = performance.now();
        this.frameId = requestAnimationFrame(() => this.onFrame());
      }
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
      const distance = 100 - progress * 100; // Element przesuwa się z 100px do 0px
      this.node.style.transform = `translateX(${distance}px)`;
      this.node.style.opacity = progress;
    }
  
    stop() {
      cancelAnimationFrame(this.frameId);
      this.startTime = null;
      this.frameId = null;
      this.duration = 0;
    }
  }
  