<?php 

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