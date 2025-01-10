function LogUsage(value: Function, context: ClassDecoratorContext) {
    const originalConstructor = value;
  
    function newConstructor(...args: any[]) {
      console.log(`Creating instance of ${context.name}`);
      return new originalConstructor(...args);
    }
  
    return newConstructor as any;
  }
  
  @LogUsage
  class Example {
    constructor(public name: string) {}
  }
  
  const instance = new Example("Test"); 
  // Logs: Creating instance of Example