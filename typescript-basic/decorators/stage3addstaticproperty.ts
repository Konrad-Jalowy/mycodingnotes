function AddStaticProperty(value: any, context: ClassDecoratorContext) {
    value.staticProperty = "I am a static property!";
    value.staticMethod = function () {
      console.log("I am a static method!");
    };
  }
  
  @AddStaticProperty
  class Example {}
  
  console.log(Example.staticProperty); // "I am a static property!"
  Example.staticMethod();              // "I am a static method!"
  