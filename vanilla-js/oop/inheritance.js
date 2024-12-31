function Person(name, age){
    this.name = name;
    this.age = age;
}

class Worker extends Person {
constructor(name, age, dept){
    super(name, age);
    this.dept = dept;
}
}

let w1 = new Worker("John", 30, "HR");
console.log(w1);
//{ name: "John", age: 30, dept: "HR" }