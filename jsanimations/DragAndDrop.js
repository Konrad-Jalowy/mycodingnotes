class Draggable {
    constructor(node) {
      this.node = node;
      this.node.style.position = "absolute";
      this.node.style.cursor = "grab";
  
      this.node.addEventListener("mousedown", (e) => this.onMouseDown(e));
    }
  
    onMouseDown(e) {
      this.startX = e.clientX - this.node.offsetLeft;
      this.startY = e.clientY - this.node.offsetTop;
  
      document.addEventListener("mousemove", this.onMouseMove);
      document.addEventListener("mouseup", this.onMouseUp);
    }
  
    onMouseMove = (e) => {
      this.node.style.left = `${e.clientX - this.startX}px`;
      this.node.style.top = `${e.clientY - this.startY}px`;
    };
  
    onMouseUp = () => {
      document.removeEventListener("mousemove", this.onMouseMove);
      document.removeEventListener("mouseup", this.onMouseUp);
    };
  }
  
  // Użycie:
  const draggable = new Draggable(document.querySelector(".draggable"));
  