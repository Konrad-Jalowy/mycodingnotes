<?php

// Klasa Adaptee (Stare API)
class OldAPI {
    public function getData(): array {
        return [
            "firstname" => "John",
            "lastname" => "Doe",
            "age" => "30", // Wiek jako string
            "id" => "12345" // ID jako string
        ];
    }
}

// Target Interface (Nowe API)
interface NewAPI {
    public function getFormattedData(): array;
}

// Adapter
class OldToNewAPIAdapter implements NewAPI {
    private OldAPI $oldAPI;

    public function __construct(OldAPI $oldAPI) {
        $this->oldAPI = $oldAPI;
    }

    public function getFormattedData(): array {
        $oldData = $this->oldAPI->getData();

        // Konwersja danych do formatu wymaganego przez Nowe API
        return [
            "fullname" => $oldData["firstname"] . " " . $oldData["lastname"],
            "age" => (int)$oldData["age"], // Konwersja wieku na liczbę
            "id" => (int)$oldData["id"]   // Konwersja ID na liczbę
        ];
    }
}

// Klient (Nowa funkcjonalność)
function useNewAPI(NewAPI $api): void {
    $data = $api->getFormattedData();
    echo "Sformatowane dane:\n";
    print_r($data);
}

// Przykład użycia
$oldAPI = new OldAPI();
$adapter = new OldToNewAPIAdapter($oldAPI);

useNewAPI($adapter);

?>