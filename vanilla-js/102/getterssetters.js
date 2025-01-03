var person = {
    firstName: "Jan",
    lastName: "Kowalski",
    
    get fullName() {
        return this.firstName + " " + this.lastName;
    },
    set fullName(fullName) {
        var parts = fullName.split(" ");

        this.firstName = parts[0];
        this.lastName = parts[1];
    }
};