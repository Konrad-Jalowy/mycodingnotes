function LogClass(value: Function, context: ClassDecoratorContext) {
    console.log(`Decorating class: ${context.name}`);
  }
  
  @LogClass
  class Example {
    field = "Hello";
    method() {
      console.log(this.field);
    }
  }