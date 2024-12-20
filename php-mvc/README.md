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