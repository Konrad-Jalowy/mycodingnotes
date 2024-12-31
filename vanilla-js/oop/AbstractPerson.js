class AbstractPerson {

    constructor(name, age){
         if(new.target === AbstractPerson){
            throw new Error("Abstract class cant be instantiated");
         }
         this.name = name; 
         this.age = age;
    }
}


class Worker extends AbstractPerson{
    constructor(name, age, dept){
        super(name, age);
        this.dept = dept;
    }
}

let worker = new Worker("John", 30, "HR");
console.log(worker);
//Object { name: "John", age: 30, dept: "HR" }

let person = new AbstractPerson("John", 30);
//Uncaught Error: Abstract class cant be instantiated