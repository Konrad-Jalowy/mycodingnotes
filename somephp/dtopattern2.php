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

// {"id":1,"name":"Jane Doe","email":"jane.doe@example.com"}