class PromiseModal {
    constructor(modalBackdrop) {
      this.modalBackdrop = modalBackdrop;
      this.modal = modalBackdrop.querySelector('.modal');
      this.cancelButton = modalBackdrop.querySelector('.btn-cancel');
      this.confirmButton = modalBackdrop.querySelector('.btn-confirm');
      this.resolve = null;

      this.init();
    }

    init() {
      this.cancelButton.addEventListener('click', () => this.close("cancel"));
      this.confirmButton.addEventListener('click', () => this.close("confirm"));
      this.modalBackdrop.addEventListener('click', (e) => {
        if (e.target === this.modalBackdrop) this.close("cancel");
      });

      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && this.modalBackdrop.style.display === 'flex') {
          this.close("cancel");
        }
      });
    }

    open(title = "Default Title", body = "Default Content") {
      this.modalBackdrop.querySelector('.modal-header').innerText = title;
      this.modalBackdrop.querySelector('.modal-body').innerText = body;

      this.modalBackdrop.style.display = 'flex';
      this.modalBackdrop.setAttribute('aria-hidden', 'false');
      this.modalBackdrop.classList.add('modal-visible');

      return new Promise((resolve) => {
        this.resolve = resolve;
      });
    }

    close(result) {
      this.modalBackdrop.style.display = 'none';
      this.modalBackdrop.setAttribute('aria-hidden', 'true');
      this.modalBackdrop.classList.remove('modal-visible');

      if (this.resolve) {
        this.resolve(result);
        this.resolve = null;
      }
    }
  }