<?php
$request = $_SERVER['REQUEST_URI'];

switch ($request) {
    case '/':
        require 'views/home.php';
        break;
    case '/about':
        require 'views/about.php';
        break;
    default:
        require 'views/404.php';
        break;
}
