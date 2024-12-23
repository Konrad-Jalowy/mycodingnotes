# PHP session
notes about session management in php


## starting session (OOP)
```php
class OOPSessionStarter {
  public static function start()
  {
    if (session_status() == PHP_SESSION_NONE) {
      session_start();
    }
  }
}
```
## starting session (no OOP)
```php
// page1.php

session_start();

echo 'Welcome to page #1';

$_SESSION['favcolor'] = 'green';
$_SESSION['animal']   = 'cat';
$_SESSION['time']     = time();

// Works if session cookie was accepted
echo '<br /><a href="page2.php">page 2</a>';

// Or maybe pass along the session id, if needed
echo '<br /><a href="page2.php?' . SID . '">page 2</a>';
```