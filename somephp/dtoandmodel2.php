<?php 
class UserDTO {
    public int $id;
    public string $name;
    public string $email;

    public function __construct(array $data) {
        foreach ($data as $key => $value) {
            if (property_exists($this, $key)) {
                $this->$key = $value;
            }
        }
    }
}

class UserModel {
    private int $id;
    private string $name;
    private string $email;

    public static function fromDTO(UserDTO $dto): self {
        $model = new self();
        foreach (get_object_vars($dto) as $key => $value) {
            if (property_exists($model, $key)) {
                $model->$key = $value;
            }
        }
        return $model;
    }

    public function toDTO(): UserDTO {
        return new UserDTO(get_object_vars($this));
    }
}

// Przykład użycia
$data = ['id' => 1, 'name' => 'Jane Doe', 'email' => 'jane@example.com'];
$dto = new UserDTO($data);
$model = UserModel::fromDTO($dto);

print_r($model);
print_r($model->toDTO());

// UserModel Object
// (
//     [id:UserModel:private] => 1
//     [name:UserModel:private] => Jane Doe
//     [email:UserModel:private] => jane@example.com
// )
// UserDTO Object
// (
//     [id] => 1
//     [name] => Jane Doe
//     [email] => jane@example.com
// )