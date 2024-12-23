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

## reading dir (piece by piece)
- is_dir - checks if directory or not
- opendir - creates directory handle
- closedir - closes directory handle
- readdir - uses directory handle to read it piece by piece
- filetype - takes file/dir and returns either "file" or "dir"
```php
$dir = "/etc/php5/";

// Open a known directory, and proceed to read its contents
if (is_dir($dir)) {
    if ($dh = opendir($dir)) {
        while (($file = readdir($dh)) !== false) {
            echo "filename: $file : filetype: " . filetype($dir . $file) . "\n";
        }
        closedir($dh);
    }
}
```