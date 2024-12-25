interface Todo3 {
    title: string;
  }
   
  const todo3: Readonly<Todo3> = {
    title: "Delete inactive users",
  };
   
// todo3.title = "Hello"; <-- cant do that