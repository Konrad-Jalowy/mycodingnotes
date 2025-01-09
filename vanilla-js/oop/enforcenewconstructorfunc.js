function Person(firstname, lastname) {
    if (!(this instanceof Person)) {
        return new Person(firstname, lastname); // Wymuszenie 'new'
    }
    this.firstname = firstname;
    this.lastname = lastname;
}

Person.prototype.sayHi = function () {
    console.log(`Hi, I'm ${this.firstname} ${this.lastname}!`);
};

const john = Person("John", "Doe"); // Działa nawet bez 'new'
john.sayHi(); // Hi, I'm John Doe!