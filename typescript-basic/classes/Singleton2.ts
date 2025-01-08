class Singleton {

    private static instance: Singleton;

    private constructor() {
        console.log("Singleton instance created.");
    }

    public static getInstance(): Singleton {
        if (!Singleton.instance) {
            Singleton.instance = new Singleton();
        }
        return Singleton.instance;
    }

    public doSomething(): void {
        console.log("Singleton is doing something!");
    }
}

const s1 = Singleton.getInstance();
s1.doSomething();

const s2 = Singleton.getInstance();

if (s1 === s2) {
    console.log("Both instances are the same!");
} else {
    console.log("Instances are different!");
}