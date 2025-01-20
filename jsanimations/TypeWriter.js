class Typewriter {
    constructor(node, text, speed = 100) {
      this.node = node;
      this.text = text;
      this.speed = speed;
      this.currentIndex = 0;
    }
  
    start() {
      this.node.textContent = ""; // Clear existing text
      this.frameId = requestAnimationFrame(() => this.type());
    }
  
    type() {
      if (this.currentIndex < this.text.length) {
        this.node.textContent += this.text[this.currentIndex];
        this.currentIndex++;
        setTimeout(() => this.type(), this.speed);
      } else {
        cancelAnimationFrame(this.frameId);
      }
    }
  }
  
  // Użycie:
  const typewriter = new Typewriter(
    document.querySelector(".typewriter"),
    "Hello, welcome to JavaScript animations!",
    100
  );
  typewriter.start();
  