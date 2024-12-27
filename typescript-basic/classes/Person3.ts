class Person3 {
    constructor(
      public name: string,
      public age: number
    ) {}
  
    public getBirthYear() {
      return new Date().getFullYear() - this.age;
    }
  }