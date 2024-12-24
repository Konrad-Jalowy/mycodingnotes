var buff = Buffer.from("Hello World");

console.log(buff); //<Buffer 48 65 6c 6c 6f 20 57 6f 72 6c 64>
console.log(buff.toString()); //Hello World

buff.write("lorem ipsum") //write overwrites!

console.log(buff.toString()) //lorem ipsum