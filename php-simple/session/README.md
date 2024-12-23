# PHP session
notes about session management in php


## Active Session Counter (last 5 mins)
Thats what we need + middleware must be called on every request. It doesnt matter if we have sess files of users that are left but their files werent destroyed somehow.
It makes sure to show how many people we have online, right now, active within 5 minutes.
```php
class OOPActiveSessionCounter {
    public static function start()
  {
    if (session_status() == PHP_SESSION_NONE) {
      session_start();
    }
  }

  
  public static function set($key, $value)
  {
    $_SESSION[$key] = $value;
  }
  
    public static function sessionsCount(){
        $session_path = session_save_path();
    
        $handle = opendir($session_path);
        $sessions = 0;
            while (($file = readdir($handle)) != FALSE) {
               
                if(in_array($file, ['.', '..']))
                    continue;
                if(!preg_match("/^sess/", $file))
                    continue;
                $sessions++;
            }
            return $sessions;
      }
      public static function sessions5Minutes(){
    
        $session_path = session_save_path();
        $handle = opendir($session_path);
        $sessions = 0;
        clearstatcache();
        static::set("_cache", (string)time());
    
            while (($file = readdir($handle)) != FALSE) {
               
                if(in_array($file, ['.', '..']))
                    continue;
                if(!preg_match("/^sess/", $file))
                    continue;
               
                $file_path = "{$session_path}/{$file}";
                $last_access = date("Y-m-d H:i:s", fileatime($file_path));
                $now = date("Y-m-d H:i:s", strtotime("-5 minutes"));
                
                if($now <= $last_access)
                    $sessions++;
                
            }
        return $sessions;
    }
    
    public static function onEveryRequestMiddleware(){
        static::start();
        static::set("_cache", (string)time());
    }
}
```

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
**session_destroy just deletes session file. it does not unset session variables or session cookie! remember**
```php
class OOPSessionCleaner {
  public static function clearAll()
  {
    session_unset();
    session_destroy();
  }
}
```

## counting sessfiles
Note:
- files are stored in a path that session_save_path() returns
- sessfiles start with SESS
- other files can be stored there too
- file is destroyed when session_destroy is called (it doesnt delete cookie or unset sess vars)
- there can be sess files with sessions that are long gone and unactive
```php
public static function sessionsCount(){
    $session_path = session_save_path();

    $handle = opendir($session_path);
    $sessions = 0;
        while (($file = readdir($handle)) != FALSE) {
           
            if(in_array($file, ['.', '..']))
                continue;
            if(!preg_match("/^sess/", $file))
                continue;
            $sessions++;
        }
        return $sessions;
  }
```

## Simple session operations (OOP)
```php
class OOPSessionSimpleHelper {
    public static function set($key, $value)
  {
    $_SESSION[$key] = $value;
  }

  
  public static function get($key, $default = null)
  {
    return isset($_SESSION[$key]) ? $_SESSION[$key] : $default;
  }

  
  public static function has($key)
  {
    return isset($_SESSION[$key]);
  }

  
  public static function clear($key)
  {
    if (isset($_SESSION[$key])) {
      unset($_SESSION[$key]);
    }
  }
}
```