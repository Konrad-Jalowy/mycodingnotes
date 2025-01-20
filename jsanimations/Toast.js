class Toast {
    constructor(container) {
      this.container = container;
    }

    show(type, message, duration = 3000) {
      const toast = document.createElement('div');
      toast.className = `toast toast-${type}`;
      toast.innerHTML = `
        ${message}
        <button class="toast-close">&times;</button>
      `;

      // Add event listener to close button
      const closeButton = toast.querySelector('.toast-close');
      closeButton.addEventListener('click', () => this.removeToast(toast));

      // Append to container
      this.container.appendChild(toast);

      // Auto-remove after the specified duration
      setTimeout(() => this.removeToast(toast), duration);
    }

    removeToast(toast) {
      toast.style.animation = 'fade-out 0.5s ease';
      toast.addEventListener('animationend', () => {
        toast.remove();
      });
    }
  }

  // Initialize the Toast system
  const toastContainer = document.getElementById('toastContainer');
  const toast = new Toast(toastContainer);

  // Helper function to show a toast
  function showToast(type, message) {
    toast.show(type, message);
  }