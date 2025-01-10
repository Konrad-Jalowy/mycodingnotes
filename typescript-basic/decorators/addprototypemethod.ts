function AddPrototypeMethod(value: Function, context: ClassDecoratorContext) {
    value.prototype.greet = function () {
      console.log(`Hello from ${context.name}`);
    };
  }
  
  @AddPrototypeMethod
  class Example {}
  
  const instance = new Example();
  (instance as any).greet(); // Logs: Hello from Example