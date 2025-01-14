<?php
class UserDTO implements JsonSerializable {
    public int $id;
    public string $name;
    public string $email;

    public function __construct(array $data) {
        $this->id = $data['id'] ?? 0;
        $this->name = $data['name'] ?? '';
        $this->email = $data['email'] ?? '';
    }

    public function jsonSerialize(): array {
        return get_object_vars($this);
    }
}

// Przykład użycia
$data = [
    'id' => 1,
    'name' => 'Jane Doe',
    'email' => 'jane.doe@example.com'
];

$userDTO = new UserDTO($data);

// Serializacja do JSON
echo json_encode($userDTO);
echo PHP_EOL;

// {"id":1,"name":"Jane Doe","email":"jane.doe@example.com"}

class UserModel {
    private int $id;
    private string $name;
    private string $email;

    public function __construct(UserDTO $dto) {
        $this->id = $dto->id;
        $this->name = $dto->name;
        $this->email = $dto->email;
    }

    public function save(): bool {
        // Zapis do bazy danych
        echo "Saving user: {$this->name} ({$this->email})";
        return true;
    }
}

// Przykład użycia
$data = [
    'id' => 4,
    'name' => 'Charlie',
    'email' => 'charlie@example.com'
];

$userDTO = new UserDTO($data);
$userModel = new UserModel($userDTO);
$userModel->save();