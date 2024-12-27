class Person1 {
    name: string;
    age: number;
    instantiatedAt = new Date();
  
    constructor(name: string, age: number) {
      this.name = name;
      this.age = age;
    }
  }