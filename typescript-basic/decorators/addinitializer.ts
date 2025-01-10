function AddInitializer(value: Function, context: ClassDecoratorContext) {
    context.addInitializer(function () {
      console.log(`Instance of ${context.name} initialized`);
    });
  }
  
  @AddInitializer
  class Example {}
  
  const instance = new Example(); 
  // Logs: Instance of Example initialized
  