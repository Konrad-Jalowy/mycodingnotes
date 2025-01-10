type PipelineStep<T> = (input: T) => T;

class FormPipeline<T> {
  private steps: PipelineStep<T>[] = [];

  addStep(step: PipelineStep<T>): this {
    this.steps.push(step);
    return this;
  }

  execute(input: T): T {
    return this.steps.reduce((data, step) => step(data), input);
  }
}

// Funkcje walidacyjne
const trimFields = (form: { [key: string]: any }): typeof form => {
  const trimmed = { ...form };
  Object.keys(trimmed).forEach(key => {
    if (typeof trimmed[key] === 'string') {
      trimmed[key] = trimmed[key].trim();
    }
  });
  return trimmed;
};

const validateRequired = (requiredFields: string[]) => (form: { [key: string]: any }): typeof form => {
  requiredFields.forEach(field => {
    if (!form[field]) throw new Error(`${field} is required`);
  });
  return form;
};

const encryptPassword = (form: { [key: string]: any }): typeof form => {
  const encrypted = { ...form };
  if (encrypted.password) {
    encrypted.password = btoa(encrypted.password); // Prosta pseudo-enkrypcja
  }
  return encrypted;
};

// Pipeline przetwarzania formularzy
const formPipeline = new FormPipeline<{ [key: string]: any }>()
  .addStep(trimFields)
  .addStep(validateRequired(['name', 'email', 'password']))
  .addStep(encryptPassword);

// Przetwarzanie
try {
  const result = formPipeline.execute({
    name: ' John ',
    email: 'john@example.com ',
    password: ' secret ',
  });
  console.log(result);
  // Wynik: { name: 'John', email: 'john@example.com', password: 'c2VjcmV0' }
} catch (error) {
  console.error((error as Error).message);
}
