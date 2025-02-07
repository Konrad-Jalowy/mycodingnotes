<?php
class ServiceContainer {
    private array $services = [];

    public function register(string $name, callable $callback) {
        $this->services[$name] = $callback;
    }

    public function get(string $name) {
        return $this->services[$name]();
    }
}
$container = new ServiceContainer();

// $container->register('database', function () {
//     return new Database('mysql:host=localhost;dbname=app', 'root', '');
// });

// $container->register('userRepository', function () use ($container) {
//     return new UserRepository($container->get('database'));
// });

// $userRepository = $container->get('userRepository');
// $users = $userRepository->getUsers();
