class Timer {
    constructor(displayElement) {
      this.displayElement = displayElement;
      this.interval = null;
      this.time = 0; // Czas w sekundach
      this.isRunning = false;
    }

    formatTime(seconds) {
      const mins = Math.floor(seconds / 60).toString().padStart(2, '0');
      const secs = (seconds % 60).toString().padStart(2, '0');
      return `${mins}:${secs}`;
    }

    updateDisplay() {
      this.displayElement.textContent = this.formatTime(this.time);
    }

    start() {
      if (this.isRunning) return;

      this.isRunning = true;
      this.interval = setInterval(() => {
        this.time++;
        this.updateDisplay();
      }, 1000);
    }

    pause() {
      this.isRunning = false;
      clearInterval(this.interval);
    }

    reset() {
      this.pause();
      this.time = 0;
      this.updateDisplay();
    }

    setTargetTime(seconds) {
      this.reset();
      this.time = seconds;
      this.updateDisplay();
    }
  }

  // Inicjalizacja
  const timerDisplay = document.getElementById('timerDisplay');
  const timer = new Timer(timerDisplay);

  // Kontrolki
  const startButton = document.getElementById('startButton');
  const pauseButton = document.getElementById('pauseButton');
  const resetButton = document.getElementById('resetButton');

  // Event Listeners
  startButton.addEventListener('click', () => {
    timer.start();
    startButton.disabled = true;
    pauseButton.disabled = false;
  });

  pauseButton.addEventListener('click', () => {
    timer.pause();
    startButton.disabled = false;
    pauseButton.disabled = true;
  });

  resetButton.addEventListener('click', () => {
    timer.reset();
    startButton.disabled = false;
    pauseButton.disabled = true;
  });