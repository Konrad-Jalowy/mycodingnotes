class DynamicForm {
    constructor(container, config) {
      this.container = document.querySelector(container);
      this.config = config;
    }
  
    // Funkcja generująca formularz
    generateForm() {
      const form = document.createElement('form');
  
      this.config.fields.forEach(field => {
        if (field.section) {
          const sectionWrapper = document.createElement('fieldset');
          const sectionLegend = document.createElement('legend');
          sectionLegend.textContent = field.section;
          sectionWrapper.appendChild(sectionLegend);
  
          field.fields.forEach(subField => {
            const fieldWrapper = this.createField(subField);
            sectionWrapper.appendChild(fieldWrapper);
          });
  
          form.appendChild(sectionWrapper);
        } else {
          const fieldWrapper = this.createField(field);
          form.appendChild(fieldWrapper);
        }
      });
  
      const submitButton = document.createElement('button');
      submitButton.type = 'submit';
      submitButton.textContent = this.config.submitText || 'Submit';
      form.appendChild(submitButton);
  
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const data = Object.fromEntries(formData);
  
        if (this.config.beforeSubmit) {
          const filteredData = this.config.beforeSubmit(data);
          this.config.onSubmit(filteredData);
        } else {
          this.config.onSubmit(data);
        }
      });
  
      this.container.innerHTML = ''; // Czyść poprzednią zawartość
      this.container.appendChild(form);
  
      this.handleConditionalFields(form);
    }
  
    // Funkcja tworząca pole formularza
    createField(field) {
      const fieldWrapper = document.createElement('div');
      fieldWrapper.classList.add('field-wrapper');
  
      if (field.wrapperClass) {
        fieldWrapper.classList.add(field.wrapperClass);
      }
  
      const label = document.createElement('label');
      label.textContent = field.label;
      label.setAttribute('for', field.name);
  
      let input;
  
      if (field.type === 'textarea') {
        input = document.createElement('textarea');
      } else if (field.type === 'select' && field.options) {
        input = document.createElement('select');
        field.options.forEach(option => {
          const optionElement = document.createElement('option');
          optionElement.value = option;
          optionElement.textContent = option;
          input.appendChild(optionElement);
        });
      } else if ((field.type === 'radio' || field.type === 'checkbox') && field.options) {
        input = document.createElement('div');
        field.options.forEach(option => {
          const optionWrapper = document.createElement('div');
          const radioOrCheckbox = document.createElement('input');
          radioOrCheckbox.type = field.type;
          radioOrCheckbox.name = field.name;
          radioOrCheckbox.value = option;
          const optionLabel = document.createElement('label');
          optionLabel.textContent = option;
          optionLabel.appendChild(radioOrCheckbox);
          optionWrapper.appendChild(optionLabel);
          input.appendChild(optionWrapper);
        });
      } else {
        input = document.createElement('input');
        input.type = field.type || 'text';
      }
  
      input.name = field.name;
      input.id = field.name;
  
      if (field.className) {
        input.classList.add(field.className);
      }
  
      if (field.required) {
        input.required = true;
      }
  
      if (field.placeholder) {
        input.placeholder = field.placeholder;
      }
  
      fieldWrapper.appendChild(label);
      fieldWrapper.appendChild(input);
  
      if (field.visibleIf) {
        fieldWrapper.dataset.visibleIf = JSON.stringify(field.visibleIf);
        fieldWrapper.style.display = 'none';
      }
  
      return fieldWrapper;
    }
  
    // Obsługa warunkowego wyświetlania pól
    handleConditionalFields(form) {
      const allFields = form.querySelectorAll('.field-wrapper');
  
      const updateVisibility = () => {
        allFields.forEach(wrapper => {
          const visibleIf = wrapper.dataset.visibleIf ? JSON.parse(wrapper.dataset.visibleIf) : null;
  
          if (visibleIf) {
            const conditionsMet = Object.entries(visibleIf).every(([fieldName, expectedValue]) => {
              const field = form.querySelector(`[name="${fieldName}"]`);
              if (!field) return false;
  
              if (field.type === 'checkbox') {
                return field.checked === expectedValue;
              } else if (field.type === 'radio') {
                const selected = form.querySelector(`[name="${fieldName}"]:checked`);
                return selected && selected.value === expectedValue;
              }
  
              return field.value === expectedValue;
            });
  
            wrapper.style.display = conditionsMet ? '' : 'none';
          }
        });
      };
  
      form.addEventListener('input', updateVisibility);
      updateVisibility(); // Inicjalne ustawienie widoczności
    }
  }
  
  // Przykład użycia
  const formConfig = {
    fields: [
      {
        section: 'Personal Information',
        fields: [
          { name: 'name', type: 'text', label: 'Your Name', required: true, placeholder: 'Enter your name', className: 'large-input', wrapperClass: 'name-wrapper' },
          { name: 'email', type: 'email', label: 'Your Email', required: true, placeholder: 'Enter your email' }
        ]
      },
      {
        section: 'Additional Information',
        fields: [
          { name: 'age', type: 'number', label: 'Your Age', required: false, placeholder: 'Enter your age' },
          { name: 'bio', type: 'textarea', label: 'Your Bio', required: false, placeholder: 'Tell us about yourself' }
        ]
      },
      {
        section: 'Preferences',
        fields: [
          { name: 'isStudent', type: 'checkbox', label: 'Are you a student?' },
          { name: 'school', type: 'text', label: 'School Name', visibleIf: { isStudent: true }, placeholder: 'Enter your school name' },
          { name: 'gender', type: 'radio', label: 'Gender', options: ['Male', 'Female'], required: true },
          { name: 'hobbies', type: 'checkbox', label: 'Hobbies', options: ['Reading', 'Traveling', 'Sports'] },
          { name: 'country', type: 'select', label: 'Country', options: ['USA', 'Canada', 'UK'], required: true }
        ]
      }
    ],
    submitText: 'Register',
    beforeSubmit: (data) => {
      // Przykład filtrowania danych: usuń ukryte pola
      Object.keys(data).forEach(key => {
        const field = document.querySelector(`[name="${key}"]`);
        if (field && field.closest('.field-wrapper').style.display === 'none') {
          delete data[key];
        }
      });
      return data;
    },
    onSubmit: (data) => {
      console.log('Form submitted with data:', data);
    }
  };
  
  const dynamicForm = new DynamicForm('#form-container', formConfig);
  dynamicForm.generateForm();