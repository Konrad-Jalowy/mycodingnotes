import random
import string

def generate_password(length, num_special, num_digits, num_letters):
    """
    Generuje hasło o określonej liczbie znaków specjalnych, cyfr i liter.

    :param length: Całkowita długość hasła
    :param num_special: Liczba znaków specjalnych w haśle
    :param num_digits: Liczba cyfr w haśle
    :param num_letters: Liczba liter w haśle
    :return: Wygenerowane hasło
    """
    if num_special + num_digits + num_letters > length:
        raise ValueError("Łączna liczba znaków specjalnych, cyfr i liter przekracza długość hasła.")

    # Znaki do wykorzystania
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    digits = string.digits
    letters = string.ascii_letters

    # Tworzenie poszczególnych części hasła
    special_part = random.choices(special_chars, k=num_special)
    digit_part = random.choices(digits, k=num_digits)
    letter_part = random.choices(letters, k=num_letters)

    # Uzupełnienie hasła, jeśli długość jest większa niż suma wymaganych znaków
    remaining_length = length - (num_special + num_digits + num_letters)
    remaining_part = random.choices(special_chars + digits + letters, k=remaining_length)

    # Połączenie wszystkich części i ich wymieszanie
    password_list = special_part + digit_part + letter_part + remaining_part
    random.shuffle(password_list)

    # Konwersja na string i zwrot hasła
    return ''.join(password_list)

# Przykład użycia
total_length = 12
special_count = 3
digit_count = 4
letter_count = 5

password = generate_password(total_length, special_count, digit_count, letter_count)
print(f"Wygenerowane hasło: {password}")
