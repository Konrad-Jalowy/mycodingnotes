import "reflect-metadata";

// Dekorator "Attribute" symuluje atrybut
function Attribute(metadataKey: string, metadataValue: any): PropertyDecorator {
    return (target: Object, propertyKey: string | symbol) => {
        Reflect.defineMetadata(metadataKey, metadataValue, target, propertyKey);
    };
}

// Klasa z atrybutami
class Example {
    @Attribute("description", "This is a name field")
    public name?: string;

    @Attribute("description", "This is an age field")
    public age?: number;

    
}

// Odczytywanie atrybutów
const metadataKey = "description";

const example = new Example();
for (const key of Object.getOwnPropertyNames(example)) {
    const description = Reflect.getMetadata(metadataKey, example, key);
    if (description) {
        console.log(`Property: ${key}, Description: ${description}`);
    }
}