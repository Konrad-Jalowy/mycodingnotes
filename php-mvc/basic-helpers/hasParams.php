<?php 
function hasParams($route){
    if(!preg_match('/\{(.+?)\}/', $route)){
        return false;
    }
    return true;
}
