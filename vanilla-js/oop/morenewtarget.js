class Person {
    constructor(firstname, lastname) {
        if (new.target === Person) {
            console.log("Tworzę osobę");
        } else {
            console.log(`Tworzę specjalizowaną osobę w klasie ${new.target.name}`);
        }
        this.firstname = firstname;
        this.lastname = lastname;
    }
}

class Employee extends Person {
    constructor(firstname, lastname, position) {
        super(firstname, lastname);
        this.position = position;
    }
}

new Person("John", "Doe"); // Tworzę osobę
new Employee("Jane", "Smith", "Manager"); // Tworzę specjalizowaną osobę w klasie Employee
