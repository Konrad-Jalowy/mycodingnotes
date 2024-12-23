# php mvc router
notes on creating php mvc router

## normalize path
there are many ways ive seen i like that one
```php
class RouterNormalize
{
  
  private function normalizePath(string $path): string
  {
    $path = trim($path, '/');
    $path = "/{$path}/";
    $path = preg_replace('#[/]{2,}#', '/', $path);

    return $path;
  }

}
```