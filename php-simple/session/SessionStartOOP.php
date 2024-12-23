<?php 

class OOPSessionStarter {
  public static function start()
  {
    if (session_status() == PHP_SESSION_NONE) {
      session_start();
    }
  }
}