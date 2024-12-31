function Person(name, age){

    if(!new.target)
        return new Person(name, age);
      
    this.name = name;
    this.age = age;
  }
  
  let jim =  Person("Jim", 20);
  
  console.log(jim);
  //Object { name: "Jim", age: 20 }