// Stare API
class OldAPI {
    getData() {
        return {
            firstname: "John",
            lastname: "Doe",
            age: "30", // Wiek jako string
            id: "12345" // ID jako string
        };
    }
}

// Adapter
class OldToNewAPIAdapter {
    constructor(oldAPI) {
        this.oldAPI = oldAPI;
    }

    getFormattedData() {
        const oldData = this.oldAPI.getData();
        return {
            fullname: `${oldData.firstname} ${oldData.lastname}`,
            age: parseInt(oldData.age, 10), // Konwersja wieku na liczbę
            id: parseInt(oldData.id, 10)   // Konwersja ID na liczbę
        };
    }
}

// Klient
function useNewAPI(api) {
    const data = api.getFormattedData();
    console.log("Sformatowane dane:", data);
}

// Przykład użycia
const oldAPI = new OldAPI();
const adapter = new OldToNewAPIAdapter(oldAPI);

useNewAPI(adapter);