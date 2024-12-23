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

## function that shows what session_status is
```php
<?php
/**
 * @return bool
 */
function is_session_started()
{
    if ( php_sapi_name() !== 'cli' ) {
        if ( version_compare(phpversion(), '5.4.0', '>=') ) {
            return session_status() === PHP_SESSION_ACTIVE ? TRUE : FALSE;
        } else {
            return session_id() === '' ? FALSE : TRUE;
        }
    }
    return FALSE;
}

// Example
if ( is_session_started() === FALSE ) session_start();
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

## clearAll (OOP)
- session_unset - destroys variables
- session_destroy - destroys session data
```php
class OOPSessionCleaner {
  public static function clearAll()
  {
    session_unset();
    session_destroy();
  }
}
```