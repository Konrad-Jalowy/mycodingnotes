function RequireStaticMethod(value: Function, context: ClassDecoratorContext) {
    if (typeof value.requiredMethod !== "function") {
      throw new Error(`${context.name} must implement a static "requiredMethod".`);
    }
  }
  
  @RequireStaticMethod
  class Example {
    static requiredMethod() {
      console.log("I am implemented!");
    }
  }