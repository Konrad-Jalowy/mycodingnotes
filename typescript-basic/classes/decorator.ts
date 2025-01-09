// Interfejs bazowy
interface INapoj {
    pobierzOpis(): string;
    pobierzKoszt(): number;
}

// Konkretny komponent
class Kawa implements INapoj {
    pobierzOpis(): string {
        return "Kawa";
    }

    pobierzKoszt(): number {
        return 5.0;
    }
}

// Dekorator bazowy
abstract class NapojDekorator implements INapoj {
    protected napoj: INapoj;

    constructor(napoj: INapoj) {
        this.napoj = napoj;
    }

    pobierzOpis(): string {
        return this.napoj.pobierzOpis();
    }

    pobierzKoszt(): number {
        return this.napoj.pobierzKoszt();
    }
}

// Konkretny dekorator: Mleko
class Mleko extends NapojDekorator {
    pobierzOpis(): string {
        return `${this.napoj.pobierzOpis()}, Mleko`;
    }

    pobierzKoszt(): number {
        return this.napoj.pobierzKoszt() + 1.5;
    }
}

// Konkretny dekorator: Cukier
class Cukier extends NapojDekorator {
    pobierzOpis(): string {
        return `${this.napoj.pobierzOpis()}, Cukier`;
    }

    pobierzKoszt(): number {
        return this.napoj.pobierzKoszt() + 0.5;
    }
}

// Program
function main() {
    let kawa: INapoj = new Kawa();
    console.log(`${kawa.pobierzOpis()} - ${kawa.pobierzKoszt()} zł`);

    kawa = new Mleko(kawa);
    console.log(`${kawa.pobierzOpis()} - ${kawa.pobierzKoszt()} zł`);

    kawa = new Cukier(kawa);
    console.log(`${kawa.pobierzOpis()} - ${kawa.pobierzKoszt()} zł`);
}

main();
