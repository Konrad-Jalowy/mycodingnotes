class Person {
    firstname: string;
    lastname: string;
    age: number;
  
    constructor(firstname: string, lastname: string, age: number) {
      this.firstname = firstname;
      this.lastname = lastname;
      this.age = age;
    }
  
    getFullName(): string {
      return `${this.firstname} ${this.lastname}`;
    }
  
    isAdult(): boolean {
      return this.age >= 18;
    }
  
    toString(): string {
      return `${this.getFullName()}, Age: ${this.age}`;
    }
  }
  
  // Przykład użycia:
  const person = new Person("John", "Doe", 25);
  console.log(person.toString()); // John Doe, Age: 25
  