function Singleton(value: Function, context: ClassDecoratorContext) {
    let instance: any;
  
    return function (...args: any[]) {
      if (!instance) {
        instance = new value(...args);
      }
      return instance;
    } as any;
  }
  
  @Singleton
  class Example {
    constructor(public name: string) {}
  }
  
  const a = new Example("A");
  const b = new Example("B");
  
  console.log(a === b); // true
  console.log(a.name);  // "A"
  console.log(b.name);  // "A"
  