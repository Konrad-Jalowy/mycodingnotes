# php-mvc
Notes from some php mvc projects ive done.

## basePath func
Ive seen it somewhere and i liked it. Helps a lot in simpler projects
```php
function basePath($path = '')
{
  return __DIR__ . '/' . $path;
}
```

## super simple autoload
Sooner or later youll need composer package, but starting off in some dummy-project, trying things out, you can use such autoloading trick:
```php
spl_autoload_register(function($class){
    if(str_ends_with($class, "Controller"))
        $path = basePath("App/Controllers/$class.php");
    else 
        $path = basePath("Framework/$class.php");
    if(file_exists($path))
        require_once $path;
});
```
