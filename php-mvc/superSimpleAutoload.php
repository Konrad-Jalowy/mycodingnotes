<?php 
//if you dont use composer (you should) you can autoload like this
function basePath($path = '')
{
  return __DIR__ . '/' . $path;
}

spl_autoload_register(function($class){
    if(str_ends_with($class, "Controller"))
        $path = basePath("App/Controllers/$class.php");
    else 
        $path = basePath("Framework/$class.php");
    if(file_exists($path))
        require_once $path;
});