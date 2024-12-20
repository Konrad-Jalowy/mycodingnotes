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

## Redirect
Must know
```php
function redirect($url)
{
  header("Location: {$url}");
  exit;
}
```

## Inspect
Another function i found somewhere and liked
```php
function inspect($value)
{
  echo '<pre>';
  var_dump($value);
  echo '</pre>';
}
```

## hasParams
I needed that in one of early stages of my project, maybe useful to sb:
```php
function hasParams($route){
    if(!preg_match('/\{(.+?)\}/', $route)){
        return false;
    }
    return true;
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
