<?php
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