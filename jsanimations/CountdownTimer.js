class CountdownTimer {
    constructor(displayElement) {
      this.displayElement = displayElement;
      this.interval = null;
      this.timeLeft = 0; // Time left in seconds
      this.isRunning = false;
    }

    formatTime(seconds) {
      const mins = Math.floor(seconds / 60).toString().padStart(2, '0');
      const secs = (seconds % 60).toString().padStart(2, '0');
      return `${mins}:${secs}`;
    }

    updateDisplay() {
      this.displayElement.textContent = this.formatTime(this.timeLeft);
    }

    start(seconds) {
      if (this.isRunning) return;

      this.timeLeft = seconds || this.timeLeft;
      this.isRunning = true;

      this.interval = setInterval(() => {
        if (this.timeLeft <= 0) {
          this.pause();
          this.playBeep();
        } else {
          this.timeLeft--;
          this.updateDisplay();
        }
      }, 1000);
    }

    pause() {
      this.isRunning = false;
      clearInterval(this.interval);
    }

    reset() {
      this.pause();
      this.timeLeft = 0;
      this.updateDisplay();
    }

    playBeep() {
      const audioContext = new (window.AudioContext || window.webkitAudioContext)();
      const oscillator = audioContext.createOscillator();
      const gainNode = audioContext.createGain();

      oscillator.type = 'sine'; // Typ dźwięku (sinusoidalny)
      oscillator.frequency.setValueAtTime(440, audioContext.currentTime); // Częstotliwość (440 Hz = A4)
      gainNode.gain.setValueAtTime(0.5, audioContext.currentTime); // Głośność

      oscillator.connect(gainNode);
      gainNode.connect(audioContext.destination);

      oscillator.start();
      setTimeout(() => {
        oscillator.stop();
      }, 500); // Trwanie dźwięku w ms
    }
  }

  // Inicjalizacja
  const countdownDisplay = document.getElementById('countdownDisplay');
  const countdownTimer = new CountdownTimer(countdownDisplay);

  // Kontrolki
  const startCountdownButton = document.getElementById('startCountdownButton');
  const pauseCountdownButton = document.getElementById('pauseCountdownButton');
  const resetCountdownButton = document.getElementById('resetCountdownButton');

  // Start odliczania (np. 10 sekund)
  const START_TIME = 10;

  startCountdownButton.addEventListener('click', () => {
    countdownTimer.start(START_TIME);
    startCountdownButton.disabled = true;
    pauseCountdownButton.disabled = false;
  });

  pauseCountdownButton.addEventListener('click', () => {
    countdownTimer.pause();
    startCountdownButton.disabled = false;
    pauseCountdownButton.disabled = true;
  });

  resetCountdownButton.addEventListener('click', () => {
    countdownTimer.reset();
    startCountdownButton.disabled = false;
    pauseCountdownButton.disabled = true;
  });