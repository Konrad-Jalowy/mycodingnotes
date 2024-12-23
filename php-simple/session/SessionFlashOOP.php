<?php 

class OOPSessionFlashHelper {

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

  public static function setFlashMessage($key, $message)
  {
    self::set('flash_' . $key, $message);
  }

  
  public static function getFlashMessage($key, $default = null)
  {
    $message = self::get('flash_' . $key, $default);
    self::clear('flash_' . $key);
    return $message;
  }

  public static function clearFlashMessages(){
    foreach ($_SESSION as $key => $value){
        if(str_starts_with($key, "flash_")){
            static::clear($key);
        }
    }
  }
}