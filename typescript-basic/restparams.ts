function introduce(salutation: string, ...names: string[]): string {
    return `${salutation} ${names.join(", ")}.`;
  }

console.log(introduce("Hello", "John", "Jane", "Jim"));
//Hello John, Jane, Jim.