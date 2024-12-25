interface Todo2 {
    title: string;
    description: string;
    completed: boolean;
  }
   
  type TodoPreview2 = Pick<Todo2, "title" | "completed">;
   
  const todo2: TodoPreview2 = {
    title: "Clean room",
    completed: false,
  };