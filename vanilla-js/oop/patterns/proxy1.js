const realObject = {
    name: "Resource",
    accessLevel: 5,
  };
  
  const proxyObject = new Proxy(realObject, {
    get(target, property) {
      console.log(`Accessing property: ${property}`);
      return target[property];
    },
    set(target, property, value) {
      if (property === "accessLevel" && value < 0) {
        console.log("Access level cannot be negative!");
        return false;
      }
      target[property] = value;
      console.log(`Set property: ${property} to ${value}`);
      return true;
    },
  });
  
  // Użycie
  console.log(proxyObject.name); // Accessing property: name
  proxyObject.accessLevel = 3;  // Set property: accessLevel to 3
  proxyObject.accessLevel = -1; // Access level cannot be negative!
  