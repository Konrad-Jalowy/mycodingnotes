<?php 
function old($field) {
    return $_POST[$field] ?? '';
}
