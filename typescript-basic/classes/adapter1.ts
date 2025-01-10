// Klasa Adaptee (Stare API)
class OldAPI {
    getData(): { firstname: string; lastname: string; age: string; id: string } {
        return {
            firstname: "John",
            lastname: "Doe",
            age: "30", // Wiek jako string
            id: "12345", // ID jako string
        };
    }
}

// Target Interface (Nowe API)
interface NewAPI {
    getFormattedData(): { fullname: string; age: number; id: number };
}

// Adapter
class OldToNewAPIAdapter implements NewAPI {
    private oldAPI: OldAPI;

    constructor(oldAPI: OldAPI) {
        this.oldAPI = oldAPI;
    }

    getFormattedData(): { fullname: string; age: number; id: number } {
        const oldData = this.oldAPI.getData();

        // Konwersja danych do formatu wymaganego przez Nowe API
        return {
            fullname: `${oldData.firstname} ${oldData.lastname}`, // Łączenie firstname i lastname
            age: parseInt(oldData.age, 10), // Konwersja wieku na liczbę
            id: parseInt(oldData.id, 10),  // Konwersja ID na liczbę
        };
    }
}

// Klient (Nowa funkcjonalność)
function useNewAPI(api: NewAPI) {
    const data = api.getFormattedData();
    console.log("Sformatowane dane:", data);
}

// Przykład użycia
const oldAPI = new OldAPI();
const adapter = new OldToNewAPIAdapter(oldAPI);

useNewAPI(adapter);
