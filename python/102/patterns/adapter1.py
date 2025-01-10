class OldAPI:
    def get_data(self):
        return {
            "firstname": "John",
            "lastname": "Doe",
            "age": "30",  # Wiek jako string
            "id": "12345"  # ID jako string
        }

# Adapter
class OldToNewAPIAdapter:
    def __init__(self, old_api):
        self.old_api = old_api

    def get_formatted_data(self):
        old_data = self.old_api.get_data()
        return {
            "fullname": f"{old_data['firstname']} {old_data['lastname']}",
            "age": int(old_data["age"]),  # Konwersja wieku na liczbę
            "id": int(old_data["id"])    # Konwersja ID na liczbę
        }

# Klient
def use_new_api(api):
    data = api.get_formatted_data()
    print("Sformatowane dane:", data)

# Przykład użycia
old_api = OldAPI()
adapter = OldToNewAPIAdapter(old_api)

use_new_api(adapter)