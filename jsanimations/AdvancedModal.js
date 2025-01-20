class AdvancedModal {
    constructor(trigger, modalBackdrop) {
      this.trigger = trigger;
      this.modalBackdrop = modalBackdrop;
      this.modal = modalBackdrop.querySelector('.modal');
      this.closeButton = modalBackdrop.querySelector('.btn-close');
      this.confirmButton = modalBackdrop.querySelector('.btn-confirm');
      this.isOpen = false;

      this.init();
    }

    init() {
      this.trigger.addEventListener('click', () => this.open());
      this.closeButton.addEventListener('click', () => this.close());
      this.confirmButton.addEventListener('click', () => this.confirm());
      this.modalBackdrop.addEventListener('click', (e) => {
        if (e.target === this.modalBackdrop) this.close();
      });
      document.addEventListener('keydown', (e) => {
        if (this.isOpen && e.key === 'Escape') this.close();
      });
    }

    open() {
      this.modalBackdrop.style.display = 'flex';
      this.modalBackdrop.setAttribute('aria-hidden', 'false');
      this.modalBackdrop.classList.add('modal-visible');
      this.isOpen = true;

      // Ustaw fokus na pierwszy interaktywny element
      this.modal.querySelector('button').focus();
    }

    close() {
      this.modalBackdrop.style.display = 'none';
      this.modalBackdrop.setAttribute('aria-hidden', 'true');
      this.modalBackdrop.classList.remove('modal-visible');
      this.isOpen = false;
    }

    confirm() {
      alert('Confirmed!');
      this.close();
    }

    setContent(title, body) {
      this.modal.querySelector('.modal-header').innerText = title;
      this.modal.querySelector('.modal-body').innerText = body;
    }
  }

  // Użycie
  const modal = new AdvancedModal(
    document.getElementById('openModal'),
    document.getElementById('modalBackdrop')
  );

  // Przykład zmiany treści modala
  modal.setContent('Custom Title', 'This is a custom modal body.');