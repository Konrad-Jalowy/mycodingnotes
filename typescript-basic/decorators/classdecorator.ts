function MyDecorator(constructor: Function) {
    console.log("Dekorator dla klasy:", constructor.name);
  }
  
  @MyDecorator
  class MyClass {}
  