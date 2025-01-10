type PipelineStep = (input: string) => string;

// Klasa Pipeline
class Pipeline {
  private steps: PipelineStep[] = [];

  // Dodajemy krok do pipeline
  addStep(step: PipelineStep): this {
    this.steps.push(step);
    return this; // umożliwia łańcuchowe dodawanie
  }

  // Uruchamiamy pipeline na danych wejściowych
  execute(input: string): string {
    return this.steps.reduce((data, step) => step(data), input);
  }
}

// Funkcje reprezentujące kroki pipeline
const trim = (input: string): string => input.trim();
const toUpperCase = (input: string): string => input.toUpperCase();
const addPrefix = (prefix: string) => (input: string): string => `${prefix}${input}`;

// Tworzymy pipeline
const textPipeline = new Pipeline()
  .addStep(trim)
  .addStep(toUpperCase)
  .addStep(addPrefix("Processed: "));

// Przykład użycia
const result = textPipeline.execute("   hello world   ");
console.log(result); // "Processed: HELLO WORLD"