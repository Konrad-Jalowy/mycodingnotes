function Task(name, description, isDone){
    this.name = name;
    this.description = description;
    this.isDone = isDone;
}

function TaskBuilder() {
    
    return {
        setName: function(name) {
            this.name = name;
            return this;
        },
        setDescription: function(description) {
            this.description = description;
            return this;
        },
        setDone: function(done) {
            this.isDone = done;
            return this;
        },
        build: function () {
            return new Task(this.name, this.description, this.isDone);
        }
    }
}

let task = (new TaskBuilder()).setName("Zadanie 1")
        .setDescription("opis").setDone(true).build();
console.log(task);