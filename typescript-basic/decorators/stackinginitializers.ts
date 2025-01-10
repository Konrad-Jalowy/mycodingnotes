function NotifyCreation(value: Function, context: ClassDecoratorContext) {
    context.addInitializer(() => {
      console.log("Obiekt utworzony!");
    });
  }
  
  function AddLogging(value: Function, context: ClassDecoratorContext) {
    context.addInitializer(() => {
      console.log("Nowa instancja została zarejestrowana w systemie logowania.");
    });
  }
  
  @NotifyCreation
  @AddLogging
  class Person {
    firstname: string;
    lastname: string;
  
    constructor(firstname: string, lastname: string) {
      this.firstname = firstname;
      this.lastname = lastname;
    }
  }
  
  // Przykład użycia:
  const person1 = new Person("Alice", "Smith");
  // Konsola:
  // Obiekt utworzony!
  // Nowa instancja została zarejestrowana w systemie logowania.
  