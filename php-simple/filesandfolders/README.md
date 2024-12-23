# files and folders
Notes on php with files and folders

## cwd and chdir
self-descriptive
```php
// current directory
echo getcwd() . "\n";

chdir('cvs');

// current directory
echo getcwd() . "\n";
```

## scandir
scandir loads into memory list of files and folders (all at once) inside path given as argument.
```php
$dir    = '/tmp';
$files1 = scandir($dir);
$files2 = scandir($dir, SCANDIR_SORT_DESCENDING);

print_r($files1);
print_r($files2);
```
You can also pass sorting order as you see.