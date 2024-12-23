<?php 
class OOPSessionCleaner {
  public static function clearAll()
  {
    session_unset();
    session_destroy();
  }
}