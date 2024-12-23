# varia (PHP)
All kind of stuff i want to note but dont have idea how to categorize it.

## Include Path
### Getting include path
```php
echo get_include_path();
// Or using ini_get()
echo ini_get('include_path');
```
### Setting include path
```php
$path = '/usr/lib/pear';
set_include_path(get_include_path() . PATH_SEPARATOR . $path);
```

### Restoring include path
Only via ini_restore
```php
ini_restore('include_path');
```