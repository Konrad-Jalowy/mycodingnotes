<?php 

class OOPSessfileCounter {
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
}