interface Todo4 {
    title: string;
    description: string;
  }
   
  function updateTodo(todo: Todo4, fieldsToUpdate: Partial<Todo4>) {
    return { ...todo, ...fieldsToUpdate };
  }
   
  const todo4_1 = {
    title: "organize desk",
    description: "clear clutter",
  };
   
  const todo4_2 = updateTodo(todo4_1, {
    description: "throw out trash",
  });