class Grid {
    constructor(container, rows, cols) {
      this.container = container;
      this.rows = rows;
      this.cols = cols;
      this.render();
    }
  
    render() {
      this.container.style.display = "grid";
      this.container.style.gridTemplateRows = `repeat(${this.rows}, 1fr)`;
      this.container.style.gridTemplateColumns = `repeat(${this.cols}, 1fr)`;
  
      for (let i = 0; i < this.rows * this.cols; i++) {
        const cell = document.createElement("div");
        cell.className = "grid-cell";
        cell.style.border = "1px solid #ccc";
        cell.style.display = "flex";
        cell.style.justifyContent = "center";
        cell.style.alignItems = "center";
        cell.textContent = i + 1;
  
        cell.addEventListener("click", () => {
          cell.style.backgroundColor = "lightblue";
        });
  
        this.container.appendChild(cell);
      }
    }
  }
  
  // Użycie:
  new Grid(document.querySelector(".grid-container"), 5, 5);
  