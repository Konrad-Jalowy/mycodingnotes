class DynamicForm {
    constructor(container, config) {
      this.container = document.querySelector(container);
      this.config = config;
    }
  
    // Funkcja generująca formularz
    generateForm() {
      const form = document.createElement('form');
  
      this.config.fields.forEach(field => {
        const fieldWrapper = document.createElement('div');
        fieldWrapper.classList.add('field-wrapper');
  
        const label = document.createElement('label');
        label.textContent = field.label;
        label.setAttribute('for', field.name);
  
        let input;
        if (field.type === 'textarea') {
          input = document.createElement('textarea');
        } else {
          input = document.createElement('input');
          input.type = field.type || 'text';
        }
  
        input.name = field.name;
        input.id = field.name;
  
        if (field.required) {
          input.required = true;
        }
  
        if (field.placeholder) {
          input.placeholder = field.placeholder;
        }
  
        fieldWrapper.appendChild(label);
        fieldWrapper.appendChild(input);
        form.appendChild(fieldWrapper);
      });
  
      const submitButton = document.createElement('button');
      submitButton.type = 'submit';
      submitButton.textContent = this.config.submitText || 'Submit';
      form.appendChild(submitButton);
  
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const data = Object.fromEntries(formData);
        this.config.onSubmit(data);
      });
  
      this.container.innerHTML = ''; // Czyść poprzednią zawartość
      this.container.appendChild(form);
    }
  }
  
  // Przykład użycia
  const formConfig = {
    fields: [
      { name: 'name', type: 'text', label: 'Your Name', required: true, placeholder: 'Enter your name' },
      { name: 'email', type: 'email', label: 'Your Email', required: true, placeholder: 'Enter your email' },
      { name: 'age', type: 'number', label: 'Your Age', required: false, placeholder: 'Enter your age' },
      { name: 'bio', type: 'textarea', label: 'Your Bio', required: false, placeholder: 'Tell us about yourself' }
    ],
    submitText: 'Register',
    onSubmit: (data) => {
      console.log('Form submitted with data:', data);
    }
  };
  
  const dynamicForm = new DynamicForm('#form-container', formConfig);
  dynamicForm.generateForm();
  