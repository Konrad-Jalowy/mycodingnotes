<?php
class UserDTO {
    public int $id;
    public string $name;
    public string $email;

    public function __construct(int $id, string $name, string $email) {
        $this->id = $id;
        $this->name = $name;
        $this->email = $email;
    }
}

// Użycie
$userDTO = new UserDTO(1, "John Doe", "john@example.com");
var_dump($userDTO);
// object(UserDTO)#1 (3) {
//   ["id"]=>
//   int(1)
//   ["name"]=>
//   string(8) "John Doe"
//   ["email"]=>
//   string(16) "john@example.com"
// }
