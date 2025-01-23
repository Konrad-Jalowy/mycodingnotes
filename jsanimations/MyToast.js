class MyToast extends HTMLElement {
    constructor() {
      super();

      // Tworzymy Shadow DOM
      this.attachShadow({ mode: 'open' });

      // Kontener dla komponentu
      const container = document.createElement('div');
      container.className = 'toast';

      // Dodanie slotu na treść toasta
      const slot = document.createElement('slot');
      container.appendChild(slot);

      // Dodanie przycisku zamknięcia, jeśli jest wymagany
      this.closeButton = document.createElement('button');
      this.closeButton.className = 'toast-close';
      this.closeButton.innerHTML = '&times;';
      this.closeButton.style.display = 'none'; // Domyślnie ukrywamy
      this.closeButton.addEventListener('click', () => this.removeToast());
      container.appendChild(this.closeButton);

      // Stylizacja komponentu
      const style = document.createElement('style');
      style.textContent = `
        .toast {
          padding: 10px 20px;
          border-radius: 5px;
          color: white;
          font-family: Arial, sans-serif;
          display: inline-block;
          position: relative;
          margin: 10px 0;
          animation: fade-in 0.5s ease forwards;
        }

        .toast-success {
          background-color: green;
        }

        .toast-error {
          background-color: red;
        }

        .toast-warning {
          background-color: orange;
        }

        .toast-info {
          background-color: blue;
        }

        .toast-close {
          position: absolute;
          top: 5px;
          right: 10px;
          background: none;
          border: none;
          font-size: 16px;
          color: white;
          cursor: pointer;
        }

        @keyframes fade-in {
          from {
            opacity: 0;
            transform: translateY(-20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        @keyframes fade-out {
          from {
            opacity: 1;
          }
          to {
            opacity: 0;
          }
        }
      `;

      // Dodajemy elementy do Shadow DOM
      this.shadowRoot.append(style, container);

      // Przechowujemy główny element dla późniejszych operacji
      this.container = container;
    }

    // Wywoływane, gdy komponent jest dodawany do DOM
    connectedCallback() {
      this.initializeToast();
    }

    // Atrybuty, które chcemy obserwować
    static get observedAttributes() {
      return ['type', 'duration', 'closeable'];
    }

    // Obsługa zmian atrybutów
    attributeChangedCallback(name, oldValue, newValue) {
      if (oldValue !== newValue) {
        this.initializeToast();
      }
    }

    // Inicjalizuje wygląd i zachowanie toasta
    initializeToast() {
      // Ustawienie klasy dla typu
      const type = this.getAttribute('type') || 'info';
      this.container.className = `toast toast-${type}`;

      // Obsługa czasu trwania
      const duration = parseInt(this.getAttribute('duration') || '3000', 10);

      // Czy przycisk zamknięcia ma być widoczny
      const closeable = this.getAttribute('closeable') === 'true';
      this.closeButton.style.display = closeable ? 'block' : 'none';

      // Automatyczne usunięcie po czasie
      if (duration > 0) {
        setTimeout(() => this.removeToast(), duration);
      }
    }

    // Usuwa toast (z animacją)
    removeToast() {
      this.container.style.animation = 'fade-out 0.5s ease';
      this.container.addEventListener('animationend', () => {
        this.remove();
      });
    }
  }

  // Rejestracja komponentu
  customElements.define('my-toast', MyToast);